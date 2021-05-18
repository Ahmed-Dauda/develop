from django.shortcuts import render

def Test(request):
    return render(request, 'base/test.html')