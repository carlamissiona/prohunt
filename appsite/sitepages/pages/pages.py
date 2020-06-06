from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.template import loader
from appsite.sitepages.forms import Prosignup, Usersignup
import logging  


def indexpage(request):
    template = loader.get_template('index.html')
    context = {  'page_title' : 'Prohunt' }
    return HttpResponse(template.render(context, request))

def aboutpage(request):
    template = loader.get_template('about.html')
    context = {  'page_title' : 'Prohunt' }
    return HttpResponse(template.render(context, request))

def prosignuppage(request):  
    html = 'Register & Join Us'
    signform = Prosignup()
    if request.method == 'POST':
        signform = Prosignup(request.POST)
        if signform.is_valid():
            # logging.warning(signform.save())
            logging.warning("signform")
            return HttpResponseRedirect('/api')   
    else:
        html = 'Register & Join Us'

    return render(request, 'signup.html', {'html': html, 'form': signform}) 
def signuppage(request): 
    context = {  'page_title' : 'Prohunt' }
    signform = Usersignup()
    if request.method == 'POST':
        signform = Usersignup(request.POST)
        if signform.is_valid():
            logging.warning("signform")
            logging.warning(signform.cleaned_data['country'])
            try:
                signform.save()
            except:
              logging.warning("An exception occurred")
             
            logging.warning("signform log end")
            return HttpResponseRedirect('/api')   
    else:
        html = 'Register & Join Us'

    return render(request, 'usersignup.html', {'html': html, 'form': signform}) 