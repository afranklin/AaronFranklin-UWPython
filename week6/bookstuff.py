"""
Tutorial - The default method

Request handler objects can implement a method called "default" that
is called when no other suitable method/object could be found.
Essentially, if CherryPy2 can't find a matching request handler object
for the given request URI, it will use the default method of the object
located deepest on the URI path.

Using this mechanism you can easily simulate virtual URI structures
by parsing the extra URI string, which you can access through
cherrypy.request.virtualPath.

The application in this tutorial simulates an URI structure looking
like /users/<username>. Since the <username> bit will not be found (as
there are no matching methods), it is handled by the default method.
"""

import cherrypy
import bookdb

class Catalog:
    
    def index(self):
		books = bookdb.BookDB()
		titles = books.titles()
		for book in titles:
			yield '<a href="/'
			yield book['id']
			yield '">'
			yield book['title']
			yield '<BR>'
    index.exposed = True
    
    def default(self, code):
		books = bookdb.BookDB()
		titles = books.titles()
		f=[item for item in titles if item['id'] == code]
		if len(f)>0:
			info = books.title_info(code)
			yield "Title: "
			yield info['title']
			yield "<BR>"
			yield "Publisher: "
			yield info['publisher']
			yield '<BR>'
			yield "author: "
			yield info['author']
			yield '<BR>'
			yield "ISBN: "
			yield info['isbn']
			yield '<BR><a href="./">back</a>'
		else:
			yield "I don't have the details for that ID"
			yield '<BR><a href="./">back</a>'
#        if user == 'remi':
#            out = "Remi Delon, CherryPy lead developer"
#        elif user == 'hendrik':
#            out = "Hendrik Mans, CherryPy co-developer & crazy German"
#        elif user == 'lorenzo':
#            out = "Lorenzo Lamas, famous actor and singer!"
#        else:
#            out = "Unknown user. :-("
        
#        return '%s (<a href="./">back</a>)' % out
    default.exposed = True


cherrypy.tree.mount(Catalog())


if __name__ == '__main__':
    import os.path
    thisdir = os.path.dirname(__file__)
    cherrypy.quickstart(config=os.path.join(thisdir, 'tutorial.conf'))
