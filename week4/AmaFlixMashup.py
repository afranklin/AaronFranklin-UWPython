# Sample code to use the Netflix python client

from Netflix import *
import getopt
import time 
from datetime import datetime
from amazonproduct import API

#Netflix Keys
APP_NAME   = ''
API_KEY    = ''
API_SECRET = ''
CALLBACK = ''

#Amazon Keys
AWS_KEY = ''
SECRET_KEY = ''

def doSearch(netflix, discs, arg):
    ######################################
    # Search for titles matching a string.
    # To view all of the returned object, 
    # you can add a simplejson.dumps(info)
    ######################################  
    data = netflix.catalog.searchTitles(arg,0,2)
    for info in data:
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
    return formats
 
if __name__ == '__main__':  

    amazon_only = []

    #Get list of bestselling Amazon movies
    abestselling = []
    api = API(AWS_KEY, SECRET_KEY, 'us')
    for i in range(4):
        node = api.item_search('UnboxVideo', BrowseNode='16386761', ItemPage=i+1)
        for movie in node.Items.Item:
            abestselling.append(movie.ItemAttributes.Title)
    print abestselling

    #Query titles on Netflix and find earliest availability date. If it's in the future - it's available on Amazon but not Netflix.
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
