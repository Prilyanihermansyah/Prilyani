from django.shortcuts import render


# Create your views here.
def fp(request):
    return render(request, 'fp.html')