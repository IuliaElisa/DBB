from django.db import models
from django_quill.fields import QuillField
from django.utils import timezone
# Create your models here.
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator



class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Contributor(models.Model):
	name = models.CharField(max_length=200, null=False, unique=True)
	email = models.CharField(max_length=200, null=True)
	institution = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, unique=True,null=False)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('In progress', 'In progress'),
			('Done', 'Done'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name




class Object(models.Model):
	CATEGORY = (
			('NEO', 'NEO'),
			('Non-NEO', 'Non-NEO'),
			)
	contributor = models.ForeignKey(Contributor, null=False, on_delete= models.CASCADE)
	name = models.CharField(max_length=200, null=False)
	magnitude = models.FloatField(null=True)
	diameter = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=2000, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ForeignKey(Tag, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.name

class Article(models.Model):
		name = models.CharField(max_length = 50, unique=False)
		asteroid = models.ForeignKey(Object, null=True, on_delete= models.SET_NULL)
		author = models.ForeignKey(Contributor, null=False, on_delete= models.CASCADE)
		content = QuillField(default = '')
		title = models.CharField(max_length=255)
		tags = models.ForeignKey(Tag, null=True, on_delete= models.SET_NULL)
		post_date = models.DateField(auto_now_add=True)
		
		def __str__(self):
			return self.name


class Warning(models.Model):
		name = models.CharField(max_length = 50, unique=False)
		asteroid = models.ForeignKey(Object, null=True, on_delete= models.CASCADE)
		author = models.ForeignKey(Contributor, null=False, on_delete= models.CASCADE)
		level = models.IntegerField(default=1,validators=[ MaxValueValidator(10), MinValueValidator(0)])
		post_date = models.DateField(auto_now_add=True)
		
		def __str__(self):
			return self.name

