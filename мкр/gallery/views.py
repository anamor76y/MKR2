from django.shortcuts import render, get_object_or_404

from .models import Image

def gallery_view(request):
    image_categories = {}  # Замініть це на ваш спосіб категоризації зображень
    images = Image.objects.all()
    for image in images:
        if image.category not in image_categories:
            image_categories[image.category] = []
        image_categories[image.category].append(image)
    return render(request, 'gallery.html', {'image_categories': image_categories})


def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'image_detail.html', {'image': image})
