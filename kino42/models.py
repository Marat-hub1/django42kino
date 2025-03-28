from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    title=models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return self.title

class Country(models.Model):
    title=models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self):
        return self.title

class Artist(models.Model):
    name=models.CharField(max_length=100, verbose_name='Имя')
    info=models.TextField(verbose_name='Информация', blank=True, null=True)
    foto=models.FileField(verbose_name='Фото', blank=True, upload_to='artist/')

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    info = models.TextField(verbose_name='Информация', blank=True, null=True)
    foto = models.FileField(verbose_name='Фото', blank=True, null=True, upload_to='director/')

    def __str__(self):
        return self.name

class Podpiska(models.Model):
    title=models.CharField(max_length=100, verbose_name='Подписка')
    price=models.IntegerField(verbose_name='Стоимость')

    def __str__(self):
        return self.title

class Kino(models.Model):
    title=models.CharField(max_length=100, verbose_name='Название')
    genre=models.ManyToManyField(Genre)
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name='Страна')
    director=models.ForeignKey(Director, on_delete= models.SET_NULL, blank=True, null=True,
                               verbose_name='Режиссер')
    artist=models.ManyToManyField(Artist)
    info=models.TextField(verbose_name='Информация',blank=True, null=True)
    year=models.IntegerField(blank=True, null=True, verbose_name='Год')
    poster= models.FileField(verbose_name='Постер',blank=True, null=True, upload_to='posters/')
    rating=models.FloatField(blank=True, null=True,verbose_name='Рэйтинг')
    trailer=models.URLField(blank=True, null=True, verbose_name='Ссылка')
    podpiska=models.ForeignKey(Podpiska, on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Подписка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return f'{self.title}/{str (self.id)}/'
        return f'{self.title}/{self.id}/'
        #return f'123'
    def getOtziv(self):
        return self.otziv_set.all()

    def getFormotziv(self):
        from .forms import OtzivForm
        return OtzivForm()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_DEFAULT, default=1)
    balanse = models.IntegerField(default=1000)

    def __str__(self):
        return self.user.username

class Otziv(models.Model):
    user = models.ForeignKey (User, on_delete=models.SET_DEFAULT, default='user', verbose_name='Пользователь')
    text = models.TextField (verbose_name='отзыв')
    film = models.ForeignKey (Kino, on_delete=models.CASCADE, verbose_name='Кино')



