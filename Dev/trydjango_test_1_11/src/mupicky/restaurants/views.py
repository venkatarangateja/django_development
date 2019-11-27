# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
	some_list = list()
	for numbers in range(1,100):
		some_list.append(numbers)
	#return HttpResponse("hello")
	return render(request, "base.html", {'bool_item': True, "num": random.randint(0,1000), "some_list": some_list})
