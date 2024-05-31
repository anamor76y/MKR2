from django.test import TestCase

# Create your tests here.


from django.test import TestCase, Client
from django.urls import reverse
from .models import Image

class GalleryViewTest(TestCase):
    def test_gallery_view(self):
        client = Client()
        response = client.get(reverse('gallery_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

class ImageDetailViewTest(TestCase):
    def setUp(self):
        self.image = Image.objects.create(title='Test Image', description='Test Description')

    def test_image_detail_view(self):
        client = Client()
        response = client.get(reverse('image_detail', args=(self.image.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_detail.html')
