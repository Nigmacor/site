from django.db import models

# Create your models here.
class Orders(models.Model):
	"""заказы, на личной странице"""
	title = models.CharField(max_length=150, db_index=True)
	costomer = models.CharField(max_length=150, db_index=True) #ссылка на заказчика
	body = models.TextField(blank=False, db_index=True)
	date_pud = models.DateTimeField(auto_now_add=True)
	date_tender_end = models.DurationField()#длительность тендора
		
	def __str__(self):
		return '{}'.format(self.title)