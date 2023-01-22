from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page',
        'values': ['Wow', 'nro', '124'],
        'obj': {
            'cars':'audi',
            'ha':'123'
        }
    }
    return render(request, 'haha/index.html', data)


def about(request):
    return render(request, 'haha/about.html')
