from django.shortcuts import render

posts = [
    {
        'author': 'Cajero 1',
        'title': 'Ultima Transacción',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Cajero 2',
        'title': 'Prestamos Por Vencer',
        'content': 'Alerta',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
