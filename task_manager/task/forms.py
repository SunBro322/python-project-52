class TaskForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': 10}),
        required=False,
        label="Метки"
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']