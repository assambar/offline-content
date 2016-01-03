# offline-content
Server for simple browsing and playing of offline multimedia in intranet.

1. Install django
2. python manage.py createsuperuser
    Create some admin user to use with your local db
2. python manage.py runserver 0.0.0.0:8000
3. Go do /admin to add a directory. Just add the path

Paths in the browser
 - browse/ - lists all dirs
 - browse/dir/<dir_id> - list of served dirs on server
 - browse/show/<file_id> - opens player for video file or web pdf reader
 - browse/raw/<file> - raw serving of the file (with streaming response)
 - browse/raw/<file>/stream - raw serving of the file (with streaming)
 - admin - django native ui to modify dirs