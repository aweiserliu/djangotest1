import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# setting.py

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "apptest1", "image", "uploud")
print(MEDIA_ROOT)
# urls.py
# url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),


# http
# http://127.0.0.1:8000/media/wx20180419.png
