from django.shortcuts import render, render_to_response

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404



def index(request):
    return render(request, 'surova/index.html')
