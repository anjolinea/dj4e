from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.
def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse("""This is a site to test out cookies. Check it out using inspect! It'll be under dj4e_cookie and sessionid. <br>
                           view count="""+str(num_visits)+"<br> Who is the most annoying child?"+num_visits*"Jacob")
    resp.set_cookie('dj4e_cookie', '7cc532d7', max_age=1000)
    return resp


