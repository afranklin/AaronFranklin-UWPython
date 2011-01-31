from amazonproduct import API

AWS_KEY = 'AKIAJM5FTNAKE7VWQYTA'
SECRET_KEY = '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'
newmovies = []

api = API(AWS_KEY, SECRET_KEY, 'us')

for i in range(10):
    node = api.item_search('UnboxVideo', BrowseNode='16386761', ItemPage=i+1)
    for movie in node.Items.Item:
        newmovies.append(movie.ItemAttributes.Title)

#total_results = node.Items.TotalResults.pyval
#total_pages = node.Items.TotalPages.pyval
#print total_results
#print total_pages

print newmovies
