# Sample code to use the Netflix python client

from Netflix import *
import getopt
import time 
from datetime import datetime
from amazonproduct import API

#Netflix IDs
APP_NAME   = 'pythonapihomework'
API_KEY    = '6w9g2g3pw8yc4chft8vxe3ve'
API_SECRET = 'rD7ZK9MekD'
CALLBACK = ''

#Amazon IDs
AWS_KEY = 'AKIAJM5FTNAKE7VWQYTA'
SECRET_KEY = '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'

def doSearch(netflix, discs, arg):
    ######################################
    # Search for titles matching a string.
    # To view all of the returned object, 
    # you can add a simplejson.dumps(info)
    ######################################  
    data = netflix.catalog.searchTitles(arg,0,2)
    for info in data:
#        print info['title']['regular']
        discs.append(info)

def getTitleFromID(netflix,arg):
    ######################################
    # Grab a specific title from the ID. 
    # The ID is available as part of the
    # results from most queries (including
    # the ones above.
    ######################################  
    movie = netflix.catalog.getTitle(arg)
    return movie

def getTitleInfo(netflix,movie):
    ######################################
    # You can retrieve information about 
    # a specific title based on the 'links'
    # which include formats, synopsis, etc.
    ######################################  
    disc = NetflixDisc(movie['catalog_title'],netflix)
    formats = disc.getInfo('formats')
#    print "Formats: %s" % simplejson.dumps(formats,indent=4)
    return formats

#    print "*** And the synopsis ***"
#    synopsis = disc.getInfo('synopsis')
#    print "Synopsis: %s" % simplejson.dumps(synopsis, indent=4)

#    print "*** And the cast ***"
#    cast = disc.getInfo('cast')
#    print "Cast: %s" % simplejson.dumps(cast, indent=4)

 
if __name__ == '__main__':  

    amazon_only = []
    today = datetime.now()

    #Get list of bestselling Amazon movies
    abestselling = []
    api = API(AWS_KEY, SECRET_KEY, 'us')
    for i in range(4):
        node = api.item_search('UnboxVideo', BrowseNode='16386761', ItemPage=i+1)
        for movie in node.Items.Item:
            abestselling.append(movie.ItemAttributes.Title)
    print abestselling

    #Query on Netflix and find the earliest availability date.  If it's in the future - it's available on Amazon but not Netflix.
    netflixClient = NetflixClient(APP_NAME, API_KEY, API_SECRET, CALLBACK, 'False')
    
    for film in abestselling:
        discs = []
        time.sleep(1)# Note that we have to sleep between queries to avoid the per-second cap on the API
        doSearch(netflixClient, discs, film)
        time.sleep(1)
        movie = getTitleFromID(netflixClient,discs[0]['id'])
        time.sleep(1)
        formats = getTitleInfo(netflixClient,movie)
        first_avail_unix = formats['delivery_formats']['availability'][0]['available_from']
        for i in range(len(formats['delivery_formats']['availability'])):
            avail_unix = formats['delivery_formats']['availability'][i]['available_from']
            print datetime.fromtimestamp(float(avail_unix))
            if float(avail_unix) < float(first_avail_unix):
                first_avail_unix = avail_unix
        avail = datetime.fromtimestamp(float(first_avail_unix))
        print str(discs[0]['title']['regular']), avail
        if datetime.now() < avail:
            amazon_only.append([str(discs[0]['title']['regular']),avail])

    print "Movies available on Amazon, but not on Netflix:"
    if amazon_only == []:
        print "None right now - try again next week!"
    else:
        for title, avail in amazon_only:
            print title, avail
