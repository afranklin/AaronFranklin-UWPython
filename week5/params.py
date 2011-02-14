import sys, time, json

params = []
for param in sys.argv:
   params.append(param)

a = int(params[1])
b = int(params[2])

print json.dumps({'result':a+b, 'uwnetid': 'afrankli', 'time':time.time()}, sort_keys=False, indent=4)
