from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request,'webapp/home1.html')

	
def contact(request):
    return render(request, 'webapp/contact.html',{'content':['If you would like to contact me, please email me.','techienest.ashish@gmail.com']}
)

	
def about(request):
    return render(request, 'webapp/about.html')
