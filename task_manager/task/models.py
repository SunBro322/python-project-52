class Task(models.Model):
    ...
    labels = models.ManyToManyField(
        'labels.Label',
        blank=True,
        verbose_name="Метки"
    )
    def get_labels_display(self):
        return ", ".join(label.name for label in self.labels.all())