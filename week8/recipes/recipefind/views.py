from django.shortcuts import render_to_response, get_object_or_404
from recipefind.models import Recipe

def index(request):
    recipe_list = Recipe.objects.all().order_by('name')[:5]
    return render_to_response('recipefind/index.html', {'recipe_list': recipe_list})

def detail(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    return render_to_response('recipefind/detail.html', {'recipe': r})

def ingredient(request, ingredient):
    recipe_list = Recipe.objects.filter(main_ingredient=ingredient)
    return render_to_response('recipefind/ingredient.html', {'recipe_list': recipe_list, 'main_ingredient':ingredient})