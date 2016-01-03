from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from .models import BaseDirectory, FileRecord

def index(request):
    base_dirs_list = BaseDirectory.objects.all()
    template = loader.get_template('browse/index.html')
    context = {
        'base_dirs_list': base_dirs_list,
    }
    return HttpResponse(template.render(context, request))


import os
depth=0
def filesInDir(dir):
    links=[]
    for dirname, dirnames, filenames in os.walk(unicode(dir)):
        for subdirname in dirnames:
            try:
                subdirPath = os.path.join(unicode(dirname), unicode(subdirname))
                links += filesInDir(subdirPath)
            except UnicodeDecodeError:
                links += ['INVALID UNICODE/ASCI path for %s in %s' % (subdirname, dirname)]

        # print path to all filenames.
        for filename in filenames:
            try:
                links += [os.path.join(unicode(dirname), unicode(filename))]
            except UnicodeDecodeError:
                links += ['INVALID UNICODE/ASCI path for %s in %s' % (filename, dirname)]
    
    return links

from datetime import datetime
import mimetypes
def dirContent(request, dir_id, refresh):
    try:
        base_dir = BaseDirectory.objects.get(pk=dir_id)
        if refresh or base_dir.filerecord_set.count() == 0:
            base_dir.filerecord_set.all().delete()
            files = filesInDir(base_dir.dir_path)
            for filePath in files:
                base_dir.filerecord_set.create(
                    file_path=filePath,
                    mime_type = mimetypes.guess_type(filePath)[0],
                    date_modified=datetime.now())

    except BaseDirectory.DoesNotExist:
        raise Http404("BaseDirectory does not exist")
    return render(request, 'browse/dir.html',
                    {'base_dir': base_dir})

from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
chunk_size = 8192

def downloadFile(request, file_id):
    fileRecord = FileRecord.objects.get(pk=file_id)
    response = HttpResponse(FileWrapper(file(fileRecord.file_path), chunk_size),
                                     content_type=fileRecord.mime_type)
    response['Content-Length'] = os.path.getsize(fileRecord.file_path)    
    response['Content-Disposition'] = "attachment; filename=%s" % fileRecord.file_path

    return response

def streamFile(request, file_id):
    fileRecord = FileRecord.objects.get(pk=file_id)
    response = StreamingHttpResponse(FileWrapper(file(fileRecord.file_path), chunk_size),
                                     content_type=fileRecord.mime_type)
    response['Content-Length'] = os.path.getsize(fileRecord.file_path)    
    response['Content-Disposition'] = "attachment; filename=%s" % fileRecord.file_path

    return response

def showFile(request, file_id):
    fileRecord = FileRecord.objects.get(pk=file_id)
    template = 'browse/default.html'
    if 'video' in fileRecord.mime_type:
        template = 'browse/video.html'
    elif 'pdf' in fileRecord.mime_type:
        template = 'browse/pdf.html'
    return render(request, template,
                    {'file': fileRecord})