import django_filters
from .models import Task
from statuses.models import Status
from labels.models import Label
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус'
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель'
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка'
    )
    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        label='Только мои задачи',
        widget=forms.CheckboxInput
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
