from django.db import models

# Create your models here.
class Student(models.Model): 
	roll=models.IntegerField()
	name=models.CharField(max_length=50)
	addr=models.CharField(max_length=50)

class Book(models.Model):
	
	name=models.CharField(max_length=50)
	price=models.IntegerField()

	
	
class Author(models.Model):
	bk_name= models.ForeignKey(Book, on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	addr=models.CharField(max_length=50)

	
	
class Meta:  
    db_table = "student"  
