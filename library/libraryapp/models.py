from django.db import models

# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length = 200, blank = True)

	def __str__(self):
		return self.title

	def to_json(self):
		return{
			'id' : self.id,
			'title' : self.title,
		}

class Book(models.Model):
	title = models.CharField(max_length = 200, blank = True)
	author = models.CharField(max_length = 200, blank = True)
	updated_at = models.DateTimeField(auto_now = True, blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add = True, blank = True, null = True)
	category_id = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)

	def __str__(self):
		return self.title

	def to_json(self):
		return{
			'id' : self.id,
			'title' : self.title,
			'author' : self.author,
			'updated_at' : self.updated_at,
			'created_at' : self.created_at,
			'category_id' : self.category_id.to_json(),
		}