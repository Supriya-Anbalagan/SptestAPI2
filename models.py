from django.db import models
class Login(models.Model):
 username=models.charField(max_length=20)
 password=models.charField(max_length=25)
