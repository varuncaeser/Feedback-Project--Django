from typing import Any
from django import forms

class Feedbackform(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)#TO GET THE FEEDBACK
    def clean_name(self):
        n=self.cleaned_data['name']
        if(len(n)<5):
            raise forms.ValidationError("Min number of Character must be >5")
        return n
    def clean_rollno(self):
        r=self.cleaned_data['rollno']
        if r<=0:
            raise forms.ValidationError("Roll number should be > 0")
        return r

