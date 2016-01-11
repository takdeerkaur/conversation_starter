from django.db import models


class Category(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	category_name = models.TextField()
	class Meta:
		ordering = ('created',)
