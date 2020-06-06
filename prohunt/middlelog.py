class ExceptionLoggingMiddleware(object):

	def process_request(self, request):
	    print(request.body )
	    print(request.method)
	    print(request.META)
	    return None