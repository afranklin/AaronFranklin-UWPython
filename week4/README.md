# Overview

AmaFlixMashup.py produces a list of videos that can be rented on demand through Amazon, but are not yet available in any form on Netflix.  Methodology:
1) Amazon API: returns the 40 bestselling video on demand titles
2) Netflix API: queries each title, and pulls the earliest release date in any format.
3) Returns titles available on Amazon that have a Netflix release date in the future.

# Sample Output (run 1/30/2011)

Movies available on Amazon, but not on Netflix:
Machete 2011-01-31 16:00:00
The Social Network 2011-02-07 16:00:00
Catfish 2011-01-31 16:00:00

# Required Modules
1) lxml: http://pypi.python.org/pypi/lxml/
2) setuptools: http://pypi.python.org/pypi/setuptools
3) python amazon product api: http://pypi.python.org/pypi/python-amazon-product-api
4) oauth: https://github.com/simplegeo/python-oauth2
5) pyflix: http://code.google.com/p/pyflix/

# Known Errors
* error if film does not yet have a date assigned in Netflix.
* amazon API output may include pre-orders, which typically fall outside of the top 40.