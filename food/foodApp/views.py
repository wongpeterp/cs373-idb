from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework import generics


def home(request):
   context = RequestContext(request)
   return render_to_response('8byte_splash.html',context)

def CuisinesModel (request) :
   context = RequestContext(request)
   return render_to_response('CuisineModel.html',context)

def IngredientsModel (request) :
   context = RequestContext(request)
   return render_to_response('IngredientModel.html',context)

def RecipesModel (request) :
   context = RequestContext(request)
   return render_to_response('RecipeModel.html',context)

def Ingredients (request) :
   context = RequestContext(request)
   return render_to_response('Ingredients.html',context)

def Cuisines (request) :
   context = RequestContext(request)
   return render_to_response('Cuisines.html',context)

def Recipes (request) :
   context = RequestContext(request)
   return render_to_response('Recipes.html',context)

def American (request) :
   context = RequestContext(request)
   return render_to_response('American.html',context)

def Italian (request) :
   context = RequestContext(request)
   return render_to_response('Italian.html',context)

def About (request) :
   context = RequestContext(request)
   return render_to_response('about.html',context)

def Index1 (request) :
   context = RequestContext(request)
   return render_to_response('Index1.html',context)

def Index2 (request) :
   context = RequestContext(request)
   return render_to_response('Index2.html',context)

def recipe_page (request) :
   context = RequestContext(request)
   return render_to_response('recipe_page.html',context)

<<<<<<< HEAD
"""
def recipes(request): 

   #Implement try except block later  

   context = RequestContext(request)
   recipes = Recipes.objects.all.order_by('name')
"""





=======
def cuisine_page (request) :
   context = RequestContext(request)
   return render_to_response('cuisine_page.html',context)
>>>>>>> 8094ac19ed8fa4e37cee2f01b64ca9d06e1dee54
                        
