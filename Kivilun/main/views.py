from django.shortcuts import render

def index(request):
    data = {
        'title': 'Ставропольские новости',
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')