from django.db import models


class rubric(models.Model):
	title = models.CharField(max_length=200)

	def get_absolute_url(self):
		return '/%s/'%self.title

class content(models.Model):
	first_table = models.ForeignKey(rubric, on_delete = models.CASCADE)
	kod = models.IntegerField()
	date = models.DateField()
	price = models.IntegerField()

