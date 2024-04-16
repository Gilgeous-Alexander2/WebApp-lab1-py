from django.shortcuts import render
from datetime import date


def GetTutors(request):
    return render(request, 'tutors.html',  
    { 'data' : {'current_date': date.today(),'abc': 123,
    'teachers': [{'name1': 'Беляев ','name2': 'Игорь Сергеевич','rank1':'Доцент','rank2':'Зав. кафедрой','id':1},
               {'name1': 'Беляев','name2': 'Игорь Сергеевич','rank1':'Доцент','rank2':'','id':2},
               {'name1': 'Беляев','name2': 'Игорь Сергеевич','rank1':'Доцент','rank2':'','id':3},
               {'name1': 'Беляев','name2': 'Игорь Сергеевич','rank1':'Доцент','rank2':'','id':4}]}})

def GetTutor(request, id):
    return render(request, 'tutor.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        }})