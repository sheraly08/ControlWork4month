from django import forms

from tasks.models import Task

# class ArticleForm(forms.Form):
#     title = forms.CharField(min_length=5, max_length=100)
#     text = forms.Textarea()
#     rate = forms.IntegerField(min_value=0, max_value=10)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "status")