# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import userinput
from .ttt import find_n_most_frequent_words


def index(request):
    user_input = userinput()
    return render(request, "index.html", {'input_n': user_input})

def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        n = user_input.cleaned_data['q']
        print n
        data = find_n_most_frequent_words(n)
        print data
        return render(request, "index.html", {'input_n': user_input, 'all_objects': data})
    return render(request, "index.html", {'input_n': user_input})