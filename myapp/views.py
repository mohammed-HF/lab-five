from django.shortcuts import render
from django.http import HttpResponseRedirect

people = []  

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

      
        person = Person(username=username, password=password)
        people.append(person)

        return HttpResponseRedirect('/add/')  
    else:
        return render(request, 'myapp/add.html')

def default(request):
    return render(request, 'myapp/default.html', {'people': people})
