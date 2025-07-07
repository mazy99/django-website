from .models import News
from django.forms import ModelForm, TextInput, DateInput, Textarea



class NewsForm(ModelForm):  
    class Meta:
        model = News
        fields = '__all__'

        widgets = {
           "title": TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Название статьи'
           }),
           "anons": TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Анонс статьи'
           }),
           "date": DateInput(attrs={
               'class': 'form-control',
               'type': 'datetime-local',
               'placeholder': 'Дата и время публикации'
           }),
           "text": Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Текст статьи'
           })
        }