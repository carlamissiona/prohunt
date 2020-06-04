from django.db import models



class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    birth_date = models.DateTimeField('birth date')
    last_login_date = models.DateTimeField('last login date')
    signup_date = models.DateTimeField('signup date')


class Consultants(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    birth_date = models.DateTimeField('birth date')
    last_login_date = models.DateTimeField('last login date')
    signup_date = models.DateTimeField('signup date')


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=40)
    pub_date = models.DateTimeField('publish date')


class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish date')
