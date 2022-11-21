from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=10)
    anxiety = models.CharField(max_length=10)
    depression = models.CharField(max_length=10)
    panic_attack = models.CharField(max_length=10)
    seeked_specialist = models.CharField(max_length=10)
    smoking = models.CharField(max_length=10)
    drinking = models.CharField(max_length=10)
    drugs = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + '- [{}]'.format(str(self.date_time))
