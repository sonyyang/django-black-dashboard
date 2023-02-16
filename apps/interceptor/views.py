from django.shortcuts import redirect, render
from django.template import RequestContext
from .forms import AddressForm

def address_view(request):
    form = AddressForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            address = form.cleaned_data.get("address")
            request.session['has_visited'] = True
            return redirect("/")
            # TODO: save address to db

    return render(request, "home/address.html", {"form": form, "msg": msg})
