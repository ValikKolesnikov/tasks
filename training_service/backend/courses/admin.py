from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.ReadingMaterial)
admin.site.register(models.Test)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Participation)
admin.site.register(models.TestProgress)
admin.site.register(models.ReadingMaterialProgress)
admin.site.register(models.CourseProgress)
admin.site.register(models.QuestionProgress)
