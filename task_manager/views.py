from django.db.models import Q
from django.contrib import messages

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users')

    def test_func(self):
        return self.request.user == self.get_object()

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        # Проверка связанных задач
        if Task.objects.filter(Q(author=user) | Q(executor=user)).exists():
            messages.error(
                request,
                'Невозможно удалить пользователя, так как он связан с задачами'
            )
            return redirect('users')
        return super().post(request, *args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Фильтр по статусу
        if status_id := self.request.GET.get('status'):
            queryset = queryset.filter(status_id=status_id)
        # Фильтр по исполнителю
        if executor_id := self.request.GET.get('executor'):
            queryset = queryset.filter(executor_id=executor_id)
        return queryset