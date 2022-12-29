from django.core.files.storage import FileSystemStorage

from Powerbank import settings
from api.v1.images.models import Image
from utils.utils import parse_bool


def upload_image(request):
    f = request.FILES['image']
    compress = parse_bool(s=request.query_params.get('compress'), val=False)
    image = Image.objects.create(image=f)
    if compress:
        image.compress()
    return image

