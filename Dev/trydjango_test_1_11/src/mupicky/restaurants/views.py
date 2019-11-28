# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import random

# def home(request):
# 	Even_list = list()
# 	odd_list = list()
# 	condition_statement = 'is enabled'
# 	if condition_statement == 'is enabled':
# 		for numbers in range(1,random.randint(0,10000)):
# 			if numbers%2 == 0:
# 				Even_list.append(numbers)
# 		context = {
# 				"Even_list": Even_list,
# 				"bool_item": True,
# 				"condition_statement": "is enabled"
# 				}
# 		return render(request, "home.html", context)
#
# 	elif condition_statement == 'is not enabled':
# 		for num in range(0,1000):
# 			if num%2 == 1:
# 				odd_list.append(num)
# 		context = {
# 				"odd_list": odd_list,
# 				"bool_item": True,
# 				"condition_statement": "is not enabled"
# 				}
# 		return render(request,"home.html",context)
#
# def about(request):
# 	return render(request,"about.html",context={})
#
# def contact(request):
# 	return render(request,"contact.html",context={})

class HomeView(TemplateView):
	template_name = "home.html"
	def get_context_data(self, *args, **kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		Even_list = list()
		odd_list = list()
		condition_statement = 'is not enabled'
		if condition_statement == 'is enabled':
			for numbers in range(1, random.randint(0, 10000)):
				if numbers % 2 == 0:
					Even_list.append(numbers)
			context = {
					"Even_list": Even_list,
					"bool_item": True,
					"condition_statement": "is enabled"
					}
			return context

		elif condition_statement == 'is not enabled':
			for num in range(0, 1000):
				if num % 2 == 1:
					odd_list.append(num)
			context = {
					"odd_list": odd_list,
					"bool_item": True,
					"condition_statement": "is not enabled"
					}
			return context