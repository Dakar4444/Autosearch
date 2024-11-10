from datetime import date
import os
from tabnanny import verbose
from django.db import models



class Catalogs(models.Model):
    gos_number = models.CharField(max_length=10, unique=False, blank=True, null=True, verbose_name='Гос. номер')
    slug = models.TextField(max_length=200, unique=False, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, unique=False, null=True, verbose_name='Описание')
    data_photo = models.DateField(default=date.today, verbose_name='Дата фото')
    is_approved = models.BooleanField(default=False, verbose_name='Одобрено / Не одобрено')

    class Meta:
        db_table = 'catalog'
        verbose_name = 'Авто'
        verbose_name_plural = 'Автомобили'

    def delete(self, *args, **kwargs):
        # Удаляем все связанные фотографии
        for photo in self.photos.all():
            photo.delete()  # Это вызовет метод delete из модели Gallery
        super().delete(*args, **kwargs)



class Gallery(models.Model):
    photo = models.ImageField(upload_to='catalogs_images', max_length=100, null=True, verbose_name='Фото')
    catalogs = models.ForeignKey(Catalogs, on_delete=models.CASCADE, related_name='photos')

    class Meta:
        db_table = 'gallery'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def delete(self, *args, **kwargs):
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super().delete(*args, **kwargs)