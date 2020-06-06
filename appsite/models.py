from django.db import models



class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    birth_date = models.DateTimeField('birth date',null=True) 
    signup_date = models.DateTimeField('signup date',auto_now_add=True)


class Consultants(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    birth_date = models.DateTimeField('birth date',null=True) 
    signup_date = models.DateTimeField('signup date',auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=40)
    pub_date = models.DateTimeField('publish date', auto_now_add=True)
 


class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish date',auto_now_add=True)
