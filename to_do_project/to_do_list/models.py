from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name


class TODO(models.Model):
    class Meta:
        verbose_name = 'TODO'
        verbose_name_plural = "TODOs"

    text = models.CharField('Text', max_length=300)
    date = models.DateTimeField("DateTime", auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text
