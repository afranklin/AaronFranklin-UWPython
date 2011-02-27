from recipefind.models import Recipe, Ingredient, Instructions
from django.contrib import admin

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3

class InstructionsInline(admin.TabularInline):
    model = Instructions
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'pub_date']}),
        ('Details', {'fields': ['main_ingredient', 'prep_time', 'cook_time']}),
    ]
    inlines = [IngredientInline, InstructionsInline]
    list_display = ('name', 'main_ingredient', 'time_required', 'prep_time', 'cook_time')
    list_filter = ['main_ingredient']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

admin.site.register(Recipe, RecipeAdmin)