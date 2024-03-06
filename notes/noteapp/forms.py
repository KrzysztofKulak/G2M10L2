from django.forms import ModelForm, CharField, TextInput, SelectDateWidget, DateField
from .models import Tag, Note


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class NoteForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())
    done_at = DateField(required=False, widget=SelectDateWidget())

    class Meta:
        model = Note
        fields = ['name', 'done_at', 'description']
        exclude = ['tags']
