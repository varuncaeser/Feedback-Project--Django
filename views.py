from django.shortcuts import render
from Studentapp.forms import Feedbackform

# Create your views here.
def feedbackView(request):
    f=Feedbackform()
    if request.method=="POST":
        f=Feedbackform(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            rollno=f.cleaned_data['rollno']
            email=f.cleaned_data['email']
            feedback=f.cleaned_data['feedback']
            d={'name':name,'rollno':rollno,'email':email,'feedback':feedback}
            return render(request,'Studentapp/response.html',d)
    d={'form':f}
    return render(request,'Studentapp/feedback.html',d)


