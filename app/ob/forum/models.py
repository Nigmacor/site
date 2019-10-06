from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	user = models.URLField(max_length=150, db_index=True) 
	body = models.TextField(blank=False, db_index=True)
	date_pud = models.DateTimeField(auto_now_add=True)
	views = models.IntegerField(default=0)
	massenge = models.IntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.title)
