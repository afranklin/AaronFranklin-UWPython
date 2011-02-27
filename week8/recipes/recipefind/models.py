from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField('date added')
    main_ingredient = models.CharField(max_length=200)
    prep_time = models.IntegerField('Prep Time(minutes)')
    cook_time = models.IntegerField('Cook Time(minutes)')
    def time_required(self):
        return self.prep_time + self.cook_time
    time_required.short_description = 'Time Required (minutes)'
    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    def __unicode__(self):
        return self.ingredient

class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe)
    instructions = models.TextField(max_length=800)
    def __unicode__(self):
        return self.instructions