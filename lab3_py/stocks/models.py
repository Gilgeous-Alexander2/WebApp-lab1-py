from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.base_user import BaseUserManager 


from rest_framework.permissions import BasePermission
# Create your models here.

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, verbose_name="Является ли пользователь менеджером?")
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Uslugi(models.Model):
    name = models.CharField(max_length=150,unique=True,verbose_name="Название")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фото логотипа компании")

    def __str__(self):
        return f'{self.name}'

class Stock(models.Model):
    # company_name = models.CharField(max_length=50, verbose_name="Название компании")
    # price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена акции")
    # is_growing = models.BooleanField(verbose_name="Растет ли акция в цене?")
	STATUS_CHOICES = (
        ('Черновик', 'Pending'),
        ('Завершена', 'Approved'),
        ('Отклонена', 'Rejected'),
    )
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Черновик')
	create_date = models.DateTimeField(auto_now_add=True)
	change_date = models.DateTimeField(null=True,auto_now=True)
	end_date = models.DateTimeField(null=True)
	date_and_time = models.DateTimeField(null=True, verbose_name="Дата и время консультации")
	url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фото логотипа компании")
	user = models.ForeignKey('AppUser', related_name='user_stocks',on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Создатель заявки")
	teacher = models.ForeignKey('AppUser', related_name='teacher_stocks',on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Преподаватель")
	is_active = models.BooleanField(default=True)
	uslugi = models.ManyToManyField(Uslugi,verbose_name="Услуги")
	# subject = models.ForeignKey('Subject', related_name='teacher_subjects',on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Преподаватель")


    


class Teacher(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    email = models.EmailField(("email адрес"), unique=True,null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Subject(models.Model):
    name= models.CharField(max_length=150,unique=True)
    teacher = models.ForeignKey('AppUser',related_name="teacher_subjects", on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Преподаватель")




class AppUserManager(BaseUserManager):
	def create_user(self, email, role, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.role=role
		user.set_password(password)
		
		user.save()
		return user
	def create_superuser(self, email,role, password):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is нужен.')
		user = self.create_user(email,role, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('teacher', 'Teacher'),
    )
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50,null=True)
	last_name = models.CharField(max_length=50,null=True)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES)
	is_superuser = models.BooleanField(default=False, verbose_name="Является ли пользователь администратором?")
	is_staff = models.BooleanField(default=False, verbose_name="Является ли пользователь менеджером?")
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['role']

	objects = AppUserManager()
	
	def __str__(self):
		return self.email
	

