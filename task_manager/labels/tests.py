from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Label
from tasks.models import Task, Status

class LabelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.label = Label.objects.create(name='Важная')
        self.status = Status.objects.create(name='В работе')
        self.task = Task.objects.create(
            name='Тестовая задача',
            description='Описание',
            status=self.status,
            author=self.user
        )
        self.task.labels.add(self.label)
        self.client.login(username='testuser', password='12345')

    def test_label_delete_protected(self):
        response = self.client.post(reverse('label_delete', args=[self.label.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Label.objects.filter(pk=self.label.pk).exists())
        self.assertIn(
            'Невозможно удалить метку',
            response.content.decode()
        )