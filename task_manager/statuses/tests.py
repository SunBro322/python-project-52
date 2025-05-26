from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Status

class StatusTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.status = Status.objects.create(name='Новый')

    def test_status_list_view(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Новый')

    def test_status_create(self):
        response = self.client.post(reverse('status_create'), {'name': 'В работе'})
        self.assertRedirects(response, reverse('statuses'))
        self.assertTrue(Status.objects.filter(name='В работе').exists())

    def test_status_delete(self):
        response = self.client.post(reverse('status_delete', args=[self.status.pk]))
        self.assertRedirects(response, reverse('statuses'))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
