import os
from django.http import HttpResponse
from django.conf import settings

def logo_image(request):
    image_path = os.path.join(settings.BASE_DIR, 'logo.png')
    with open(image_path, 'rb') as f:
        image = f.read()
    return HttpResponse(image, content_type="image/png")