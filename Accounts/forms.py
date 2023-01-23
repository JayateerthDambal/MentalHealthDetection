from .models import UserResponse
from django import forms


class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['first_ques', 'second_ques', 'third_ques',
                  'fourth_ques', 'fifth_ques'
                  ]
