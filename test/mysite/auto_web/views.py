from django.shortcuts import render, HttpResponse

# Create your views here.


def t_view(request):
    print(request)
    return render(request, 't_html.html')