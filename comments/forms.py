from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)


class CommentSaveForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("user", "content", "phone")