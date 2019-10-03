from django.db import models
from datetime import timedelta


# Create your models here.
class Orders(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	costomer = models.URLField(max_length=150, db_index=True) #ссылка на заказчика
	body = models.TextField(blank=False, db_index=True)
	date_pud = models.DateTimeField(auto_now_add=True)
	duration = models.DurationField(default=timedelta(days=7))#длительность тендора
		
	def __str__(self):
		return '{}'.format(self.title)