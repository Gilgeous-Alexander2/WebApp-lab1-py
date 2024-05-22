from django.db import models
from datetime import date


# Create your models here.

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Uslugi(models.Model):
    name = models.CharField(max_length=150,unique=True)
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фото логотипа компании")

    def __str__(self):
        return f'{self.name}'

class Stock(models.Model):
    # company_name = models.CharField(max_length=50, verbose_name="Название компании")
    # price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена акции")
    # is_growing = models.BooleanField(verbose_name="Растет ли акция в цене?")
    status = models.CharField(max_length=150,default="Черновик")
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(null=True,auto_now=True)
    end_date = models.DateTimeField(null=True)
    date_and_time = models.DateTimeField(null=True, verbose_name="Дата и время консультации")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фото логотипа компании")
    user = models.ForeignKey('AuthUser', on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Создатель заявки")
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Преподаватель")
    is_active = models.BooleanField(default=True)
    uslugi = models.ManyToManyField(Uslugi,verbose_name="Услуги")

    


class Teacher(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Subject(models.Model):
    name= models.CharField(max_length=150,unique=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Преподаватель")





    




# class Teacher_Subject(models.Model):
#     teacherid = models.IntegerField(default=1)
#     predmet = models.IntegerField(default=1)





    
