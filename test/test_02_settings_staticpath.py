import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /Users/aweiser/Documents/PythonProjects/Djangosrc/djangotest1
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

print(BASE_DIR)

print(STATICFILES_DIRS)
