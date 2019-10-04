from django.db import models
from datetime import timedelta
from django.shortcuts import reverse


# Create your models here.
class Orders(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	costomer = models.URLField(max_length=150, db_index=True) #ссылка на заказчика
	body = models.TextField(blank=False, db_index=True)
	date_pud = models.DateTimeField(auto_now_add=True)
	duration = models.DurationField(default=timedelta(days=7))#длительность тендора
	clicked = models.BooleanField(default=False)
	#tag

	def get_absolute_url(self):
		return reverse('order_detail_url', kwargs={'id': self.id})

	def __str__(self):
		return '{}'.format(self.title)
