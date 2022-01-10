from django.db import models
from django.db.models.deletion import SET_NULL
from datetime import date

class Category(models.Model):
    name = models.CharField('назва категорії', max_length=100)
    description = models.TextField('опис категорії')
    image = models.ImageField('зображення до категорії', upload_to = 'category_img/')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Comment(models.Model):
    name = models.CharField('імя коментатора', max_length=100)
    text = models.TextField('текст коментаря')
    parent = models.ForeignKey('self', verbose_name='Відповідь на:', on_delete=SET_NULL, null=True, blank=True)
   
    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'

class Video(models.Model):
    name = models.CharField('назва відео', max_length=100)
    video = models.FileField(upload_to='videos/', null=True)
    description = models.TextField('опис  відео')
    image = models.ImageField('фрагмент з відео', upload_to = 'videos_img/')
    category = models.ManyToManyField(Category, verbose_name='категорія')
    like = models.PositiveIntegerField('кількість лайків', default=0)
    dislike = models.PositiveIntegerField('кількість дизлайків', default=0)
    views = models.PositiveIntegerField('кількість переглядів', default=0)
    date = models.DateField('дата завантаження', default=date.today)
    comment = models.ForeignKey(Comment, verbose_name='коментарі', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Відео'
        verbose_name_plural = 'Відео'