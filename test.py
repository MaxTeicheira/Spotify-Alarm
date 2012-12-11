from alarm import format

times = ['6:30', '6:30am', '06:30', '6:30pm',
         '12:40', '12:40am', '12:40pm', '13:30']

for t in times:
  print t
  print format(t)

