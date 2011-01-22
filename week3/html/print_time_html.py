import time
import datetime

print """<html>
<head>
 <title>Print Time</title>
</head>
<body>"""

print "Here is the time: %s" % time.time()
print "<BR>"
print "<B>and again: %s" % datetime.datetime.now()
print "</B>"
