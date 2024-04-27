from django.shortcuts import render
from datetime import date
from Proj.models import Teachers
from django.db.models import Q



def GetTutors(request):
    return render(request, 'tutors.html',  
    { 'data' : {'current_date': date.today(),'abc': 123,
    'teachers': Teachers.objects.all()}})

def GetTutor(request, id):
    return render(request, 'tutor.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        }})

def sendText(request):
    input_text = request.GET['text']
    return render(request,'consult.html',{'data':{'teachers': Teachers.objects.filter(Q(first_name=input_text)|Q(second_name=input_text)|Q(first_name=input_text))}})


def Consult(request):
    return render(request,'consult.html',{ 'data' : {'current_date': date.today(),
    'teachers': Teachers.objects.all()}})
    
