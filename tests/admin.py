from django.contrib import admin
from .models import *


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # (nice to have) you could add the related objects like questions, results to be easier to add a test
    fields = ('name', 'description')
    list_filter = ('name', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('tests', )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('text', 'score', 'question')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    filter_horizontal = ('tests', )
