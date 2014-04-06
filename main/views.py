from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django import forms

import main.models

#class SearchForm(forms.Form):
#    subject = forms.CharField(max_length=100)

# views

def search(request):
    template = loader.get_template('search.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def radha(request):
    template = loader.get_template('radha.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

#def submit(requestYp, searchtext):
def submit(request):
    print "submit"
    #subject = form.cleaned_data['subject']
    #message = form.cleaned_data['message']
    #sender = form.cleaned_data['sender']
    #cc_myself = form.cleaned_data['cc_myself']
    print request.POST
    qd = request.POST
    searchtext = qd['searchtext']
    print searchtext
    #form = SearchForm(request.POST)
    #title = None
    #if form.is_valid():
    #    print "is valid"
    #    title = form.cleaned_data['searchtext']
    #    print title
    #print title
    #a = main.models.Lake.objects.raw('select * from lake where lake.name=%s', [searchtext])
    a = main.models.Movie.objects.raw('select * from movie where movie_name=%s', [searchtext])
    print a
    results = []
    for b in a:
        results.append(b.movie_name + " " + str(b.year) + " "  + str(b.movie_id))
    print results
    #results = a[0].name + a[0].area + a[0].depth + a[0].elevation + a[0].river + a[0].coordinates

    template = loader.get_template('radha.html')
    context = RequestContext(request, {'results':results, })
    return HttpResponse(template.render(context))
