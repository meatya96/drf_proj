from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)
    preview = models.ImageField(upload_to="materials/preview", blank=True, null=True)

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(upload_to="materials/preview", blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс"
    )
