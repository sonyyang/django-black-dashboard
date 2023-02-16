from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.template import loader
from django.template import RequestContext

class AddressMiddleware(MiddlewareMixin):
    def process_request(self, request):        
        if request.user.is_anonymous == False and request.path != "/address" and request.session.get('has_visited', False) == False:
            # TODO: check the data from DB and write it to session
            return redirect("/address")
                    
        pass
