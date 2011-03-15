import cgi

import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Recipe(db.Model):
    author = db.UserProperty()
    title = db.StringProperty(multiline=False)
    time_required = db.StringProperty(multiline=False)
    main_ingredient = db.StringProperty(multiline=False)
    ingredients = db.StringProperty(multiline=True)
    instructions = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        recipes_query = Recipe.all().order('-date')
        recipes = recipes_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'recipes': recipes,
            'url': url,
            'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'index2.html')
        self.response.out.write(template.render(path, template_values))

class RecipeDetail(webapp.RequestHandler):
    def get (self):
        recipes = Recipe.gql("WHERE title = :title ORDER BY date DESC",
                                 title=self.request.query_string)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'recipes': recipes,
            'url': url,
            'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class SearchMain(webapp.RequestHandler):
    def get (self):
        recipes = Recipe.gql("WHERE main_ingredient = :main ORDER BY date DESC",
                                 main=self.request.query_string)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'recipes': recipes,
            'url': url,
            'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'filter.html')
        self.response.out.write(template.render(path, template_values))	

class AddNew(webapp.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
        }

        path = os.path.join(os.path.dirname(__file__), 'new.html')
        self.response.out.write(template.render(path, template_values))

class AddRecipe(webapp.RequestHandler):
    def post(self):
        recipe = Recipe()

        if users.get_current_user():
            recipe.author = users.get_current_user()

        recipe.title = self.request.get('title')
        recipe.time_required = self.request.get('time_required')
        recipe.main_ingredient = self.request.get('main_ingredient')
        recipe.ingredients = self.request.get('ingredients')
        recipe.instructions = self.request.get('instructions')
        recipe.put()
        self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
									  ('/detail', RecipeDetail),
									  ('/new', AddNew),
                                      ('/add', AddRecipe),
									  ('/ingredient', SearchMain)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()