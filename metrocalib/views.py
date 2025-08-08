from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'metrocalib/dashboard.html')

def index(request):
    return render(request, 'metrocalib/index.html')

def service(request):
    return render(request, 'metrocalib/service.html')

def portfolio(request):
    return render(request, 'metrocalib/portfolio.html')

def index2(request):
    return render(request, 'metrocalib/index2.html')

def about(request):
    return render(request, 'metrocalib/about.html')
def blog(request):
    return render(request, 'metrocalib/blog.html')

def contact(request):
    return render(request, 'metrocalib/contact.html')
