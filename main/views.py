from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306216636',
        'name': 'Muhammad Raihan Maulana',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)

