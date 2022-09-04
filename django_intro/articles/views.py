from django.shortcuts import render

# Create your views here.

def JJK(request):
    album = ['화양연화', 'YNWA', 'MapOfTheSoul', 'Wings']
    context = {
        'name' : '전정국',
        'age' : 26,
        'solo' : ['euphoria', '시차',],
        'album' : album
    }
    return render(request, 'JJK.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    value = request.GET.get('search')
    context = {
        'value' : value
    }
    return render(request, 'catch.html', context)

def BTS(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'BTS.html', context)