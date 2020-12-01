from django.shortcuts import render


# Render Home Page
def index(request):
    return render(request, 'index.html')


# Render Contact Us Page
def contact(request):
    return render(request, 'contact.html')
