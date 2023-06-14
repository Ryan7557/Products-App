from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs): # *args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):
    my_context = {
        "title": "this is django practice.",
        "my_number": 7557,
        "my_list": [123, 556, 762, 545, 'abc'],
        "this_is_true": True,
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, 'about.html', my_context)