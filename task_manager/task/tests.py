from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from statuses.models import Status
from labels.models import Label
from .models import Task


class TaskFilterTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.status = Status.objects.create(name='В работе')
        self.label = Label.objects.create(name='Важная')
        self.task = Task.objects.create(
            name='Тестовая задача',
            description='Описание',
            status=self.status,
            author=self.user
        )
        self.task.labels.add(self.label)
        self.client.login(username='testuser', password='12345')

    def test_filter_by_status(self):
        response = self.client.get(reverse('tasks'), {'status': self.status.pk})
        self.assertContains(response, 'Тестовая задача')

    def test_filter_by_label(self):
        response = self.client.get(reverse('tasks'), {'labels': self.label.pk})
        self.assertContains(response, 'Тестовая задача')

    def test_filter_self_tasks(self):
        # Создаем задачу другого пользователя
        other_user = User.objects.create_user(username='other', password='12345')
        Task.objects.create(name='Чужая задача', author=other_user, status=self.status)

        response = self.client.get(reverse('tasks'), {'self_tasks': 'on'})
        self.assertContains(response, 'Тестовая задача')
        self.assertNotContains(response, 'Чужая задача')