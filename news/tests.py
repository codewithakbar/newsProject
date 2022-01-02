from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='yangilik matni')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expeted_object_title = f'{post.title}'
        expeted_object_text = f'{post.text}'
        self.assertEqual(expeted_object_title, 'Mavzu')
        self.assertEqual(expeted_object_text, 'yangilik matni')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text='boshqa yangilik')

    def test_views_url_exist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_views_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

