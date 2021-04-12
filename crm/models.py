from django.db import models

class Cars(models.Model):
    cars_dt = models.DateTimeField(auto_now=True)
    cars_brand = models.CharField(max_length=20, verbose_name="Марка")
    cars_model = models.CharField(max_length=20, verbose_name='Модель')

    def __str__(self):
        return self.cars_brand

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

# Create your models here.
