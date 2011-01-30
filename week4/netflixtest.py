# Sample code to use the Netflix python client

from Netflix import *
import getopt
import time 

APP_NAME   = 'pythonapihomework'
API_KEY    = '6w9g2g3pw8yc4chft8vxe3ve'
API_SECRET = 'rD7ZK9MekD'
CALLBACK   = 'http://api.netflix.com/oauth/request_token'
        
def doSearch(netflix, discs, arg):
    ######################################
    # Search for titles matching a string.
    # To view all of the returned object, 
    # you can add a simplejson.dumps(info)
    ######################################  
    print "*** RETRIEVING MOVIES MATCHING %s ***" % arg
    data = netflix.catalog.searchTitles(arg,0,10)
    for info in data:
        print info['title']['regular']
        discs.append(info)

def doAutocomplete(netflix,arg):
    ######################################
    # Use autocomplete to retrieve titles
    # starting with a specified string.
    # To view all of the returned object, 
    # you can add a simplejson.dumps(info)
    ######################################  
    print "*** First thing, we'll search for " + arg + " as a string and see if that works ***"
    autocomplete = netflix.catalog.searchStringTitles(arg)
    print simplejson.dumps(autocomplete)
    for info in autocomplete:
        print info['title']['short']
    
def getTitleFromID(netflix,arg):
    ######################################
    # Grab a specific title from the ID. 
    # The ID is available as part of the
    # results from most queries (including
    # the ones above.
    ######################################  
    print "*** Now we'll go ahead and try to retrieve a single movie via ID string ***"
    print "Checking for " + arg
    movie = netflix.catalog.getTitle(arg)
    if movie['catalog_title']['title']['regular'] == "Flip Wilson":
        print "It's a match, woo!"
    return movie

def getTitleInfo(netflix,movie):
    ######################################
    # You can retrieve information about 
    # a specific title based on the 'links'
    # which include formats, synopsis, etc.
    ######################################  
    print "*** Let's grab the format for this movie ***"
    disc = NetflixDisc(movie['catalog_title'],netflix)
    formats = disc.getInfo('formats')
    print "Formats: %s" % simplejson.dumps(formats,indent=4)

    print "*** And the synopsis ***"
    synopsis = disc.getInfo('synopsis')
    print "Synopsis: %s" % simplejson.dumps(synopsis, indent=4)

    print "*** And the cast ***"
    cast = disc.getInfo('cast')
    print "Cast: %s" % simplejson.dumps(cast, indent=4)

  
if __name__ == '__main__':  

    netflixClient = NetflixClient(APP_NAME, API_KEY, API_SECRET, CALLBACK, verbose)
    user = None
    discs=[]
    

