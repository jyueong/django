from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    # name = 'KNJ'
    context = {
        'name' : 'KNJ',
        'age' : 20,
        'foods' : ['apple', 'orange', 'watermelon']
    }
    return render(request, 'dtl.html', context)

def greeting(request):
    context = {
        'name' : 'namjoon',
        'age' : 29,
    }
    return render(request, 'greeting.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    value = request.GET.get('search')
    name = '김남준아님알엠'
    context = {
        'value' : value,
        'name' : name,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'catch.html', context)