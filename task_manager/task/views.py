from django_filters.views import FilterView
from .filters import TaskFilter

class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.all()