from django.http import HttpResponse
from django.views import View
from django.template import loader


def indexpage(request):
    template = loader.get_template('index.html')
    context = {  'page_title' : 'Prohunt' }
    return HttpResponse(template.render(context, request))
def aboutpage(self, request):
    template = loader.get_template('about.html')
    context = {  'page_title' : 'Prohunt' }
    return HttpResponse(template.render(context, request))

# def aboutpage(self, request):
# 	template= loader.get_template('about.html')
#     context = {'page_title' : 'About'}
#     return HttpResponse(template.render(context, request))



# def articlespage(self, request):
# 	template = loader.get_template('articles.html')
#     context = {'page_title' : 'Article List'}
#     return HttpResponse(template.render(context, request))

