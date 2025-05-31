class Task(models.Model):
    ...
    labels = models.ManyToManyField(
        'labels.Label',
        blank=True,
        verbose_name="Метки"
    )