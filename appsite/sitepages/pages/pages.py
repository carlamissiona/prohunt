from django.http import HttpResponse
from django.views import View

class PageView(View):
    greeting = "Good Day"

    def about(self, request):
        return HttpResponse(self.greeting)