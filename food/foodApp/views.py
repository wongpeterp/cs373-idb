from django.shortcuts import render
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework import generics
from .models import Cuisines, Recipes, Ingredients
from .search import normalize_query, get_query

def home(request):
    context = RequestContext(request)
    return render_to_response('8byte_splash.html',context)

def about (request) :
    context = RequestContext(request)
    return render_to_response('about.html',context)

def recipes(request) : 
    context = RequestContext(request)
    recipes = Recipes.objects.all()

    context_dict = {}

    for recipe in recipes :
         recipe_dict = {}
         recipe_dict['name'] = recipe.name
         recipe_dict['id'] = recipe.recipe_id
         recipe_dict['cuisine'] = eval(recipe.cuisine_ori)
         recipe_dict['img'] = recipe.img
         recipe_dict['quant_data'] = eval(recipe.quant_data)
         recipe_dict['directions'] = recipe.directions
         recipe_dict['ingredients'] = eval(recipe.ingredient_amount)
         recipe_dict['nut_info'] = eval(recipe.nut_info)
         
         context_dict[recipe.recipe_id] = recipe_dict
 
     
    return render_to_response('recipe_model.html',{'d': context_dict}, context)

   
def recipe(request, r_name):

   context = RequestContext(request)
   recipe = Recipes.objects.get(recipe_id=r_name)
   recipe_dict = {}
   recipe_dict['name'] = recipe.name
   recipe_dict['id'] = recipe.recipe_id
   
   recipe_dict['cuisine'] = eval(recipe.cuisine_ori)
   recipe_dict['img'] = recipe.img
   recipe_dict['quant_data'] = eval(recipe.quant_data)
   
   recipe_dict['directions'] = recipe.directions
   recipe_dict['ingredients'] = eval(recipe.ingredient_amount)
   recipe_dict['nut_info'] = eval(recipe.nut_info) 
 
   return render_to_response('recipe_page.html', {'d': recipe_dict}, context)

def ingredients(request) : 
   context = RequestContext(request)
   ingredients = Ingredients.objects.all()
   
   context_dict = {}
  
   for ingredient in ingredients :
      ingredient_dict = {}
      ingredient_dict['id'] =  ingredient.ing_id
      ingredient_dict['name'] = ingredient.name
      ingredient_dict['quant_data'] = eval(ingredient.quant_data)
      ingredient_dict['nut_info'] = eval(ingredient.nut_info)
      ingredient_dict['recipes'] = eval(ingredient.all_recipes)
      ingredient_dict['cuisines'] = eval(ingredient.all_cuisines)
 
      context_dict[ingredient.ing_id] = ingredient_dict
 
   return render_to_response('ingredient_model.html',{'d': context_dict}, context)

  
   
def ingredient(request, i_name):

    context = RequestContext(request)
    ingredient = Ingredients.objects.get(ing_id=i_name)

    ingredient_dict = {}
    ingredient_dict['id'] =  ingredient.ing_id
    ingredient_dict['name'] = ingredient.name
    ingredient_dict['quant_data'] = eval(ingredient.quant_data)
    ingredient_dict['nut_info'] = eval(ingredient.nut_info)
    ingredient_dict['recipes'] = eval(ingredient.all_recipes)
    ingredient_dict['cuisines'] = eval(ingredient.all_cuisines)

    return render_to_response('ingredient_page.html',{'d':ingredient_dict}, context)
   

def cuisines(request) : 

    context = RequestContext(request)
    cuisines = Cuisines.objects.all()
    context_dict = {}   

    for cuisine in cuisines: 
        cuisine_dict = {}
        cuisine_dict['id'] = cuisine.id_cusine
        cuisine_dict['name'] = cuisine.name
        cuisine_dict['url'] = cuisine.url
        cuisine_dict['quant_data'] = eval(cuisine.quant_data)
        cuisine_dict['recipes'] = eval(cuisine.reci)
        cuisine_dict['ingredients'] = eval(cuisine.ingr)

        context_dict[cuisine.id_cusine] = cuisine_dict

   
    return render_to_response('cuisine_model.html',{'d':context_dict}, context)


     
def cuisine(request, c_name):

    context = RequestContext(request)
    cuisine = Cuisines.objects.get(id_cusine=c_name)

    cuisine_dict = {}
    cuisine_dict['id'] = cuisine.id_cusine
    cuisine_dict['name'] = cuisine.name
    cuisine_dict['url'] = cuisine.url
    cuisine_dict['quant_data'] = eval(cuisine.quant_data)
    cuisine_dict['recipes'] = eval(cuisine.reci)
    cuisine_dict['ingredients'] = eval(cuisine.ingr)

    return render_to_response('cuisine_page.html', {'d':cuisine_dict}, context)

def dprint(a):
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print(str(a))
    print("@@@@@@@@@@@@@@@@@@@@@@")

def search(request) :
    query_string = ''
    found_entries = []
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query_recipes = get_query(0,query_string, ['name','recipe_id','directions','nut_info','quant_data'])
        entry_query_recipes_and = get_query(1,query_string, ['name','recipe_id','directions','nut_info','quant_data'])
        found_entries_recipes = list(Recipes.objects.filter(entry_query_recipes).order_by('name').iterator())
        found_entries_recipes +=list(Recipes.objects.filter(entry_query_recipes_and).order_by('name').iterator())

        found_entries.append(found_entries_recipes)

        entry_query_ingredients = get_query(0,query_string, ['ing_id','name','quant_data','nut_info'])
        entry_query_ingredients_and = get_query(1,query_string, ['ing_id','name','quant_data','nut_info'])
        found_entries_ingredients = list(Ingredients.objects.filter(entry_query_ingredients).order_by('name').iterator())
        found_entries_ingredients += list(Ingredients.objects.filter(entry_query_ingredients_and).order_by('name').iterator())

        found_entries.append(found_entries_ingredients)

        entry_query_cuisines = get_query(0, query_string, ['id_cusine','name','quant_data','ingr','reci'])
        entry_query_cuisines_and = get_query(1, query_string, ['id_cusine','name','quant_data','ingr','reci'])
        found_entries_cuisines = list(Cuisines.objects.filter(entry_query_cuisines).order_by('name').iterator())
        found_entries_cuisines +=list(Cuisines.objects.filter(entry_query_cuisines_and).order_by('name').iterator())
        found_entries.append(found_entries_cuisines)

    dprint(str((found_entries[0])[1]))
    result_list = []
    for i in range(0,len(found_entries)):
        anon_list = []
        for j in range(0,len(found_entries[i])):
            anon_list.append(str(found_entries[i][j]))
        result_list.append(set(anon_list))
    
    #TODO: for each element in result list, search fields for substring
    #for item in result_list:
        #somehow access item's fields
        
    length = 0
    final_dict = {'d':found_entries,'query': query_string, 'length': length}
    return render_to_response('search.html', {'d': result_list}, context_instance=RequestContext(request))



def crossFit():

    context = RequestContext(request)

    teamApiUrl = "crossfit.social/"
    requestRegions = urllib.request.urlopen(teamApiUrl+"api/regions/?format=json")
    requestAthletes = urllib.request.urlopen(teamApiUrl+"api/athletes/?format=json")
    requestInstagrams = urlib.request.urlopen(teamApiUrl+"api/instagram/?format=json")

    responseRegions = requestDivisions.read().decode("utf-8")
    regionList = json.loads(responseDivisions)

    responseAthletes = requestAthletes.read().decode("utf-8")
    athleteList = json.loads(responseAthletes)

    responseInstagrams = requestInstagram.read().decode("utf-8")
    instagramList = json.loads(responseInstagrams)



    #this will pass in a list containing an athlete name, region, and an instagram post
    crossFitDict = {}

    #Right now we're getting all the athletes, maybe just a subset?

    for athlete in athleteList :
        crossFitDict['athlete_name'] = athlete.name
        crossFitDict['region'] = regionList[athlete.region] 
        crossFitdict['post'] = instagramList.athlete.id[athlete.id].post 
        #For each athlete have their image pop up in a box along with
        # height and affiliation and weight
        crossFitDict['img'] = athlete.img 
        crossFitDict['height'] = athlete.height
        crossFitDict['weight'] = athlete.weight



    return render_to_response('crossFit.html', {'d': crossFitDict}, context)
 
  
    






