from django import forms
from .models import Subject,Note


class SubjectCreationForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

class NoteCreationForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
