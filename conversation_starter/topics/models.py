from django.db import models
from categories.models import Category


class Topic(models.Model):
	ENTERTAINMENT = 'ENT'
	SPORTS = 'SPO'
	ART = 'ART'
	CATEGORY_OPTIONS = (
		(ENTERTAINMENT, 'Entertainment'),
		(SPORTS, 'Sports'),
		(ART, 'Art'),
		)
	created = models.DateTimeField(auto_now_add=True)
	topic_name = models.TextField()
	category = models.ManyToManyField(Category)
	# category = models.CharField(max_length=3, choices=CATEGORY_OPTIONS, default=ENTERTAINMENT)
	# owner = models.ForeignKey('auth.User', related_name='snippets')
	class Meta:
		ordering = ('created',)
