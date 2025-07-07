from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Анонс',max_length=250)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.pk}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

