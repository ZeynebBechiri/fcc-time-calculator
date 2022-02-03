def add_time(start, duration,*args):

  wd = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  AP = ["AM","PM"]

  x = start.split()
  xs = [int(i) for i in x[0].split(":")]
  xd = [int(j) for j in duration.split(":")]

  minutes = xs[1] + xd[1]
  if (minutes > 60):
    sum_hours = xs[0] + xd[0] + 1
    minutes = minutes - 60
  else:
    sum_hours = xs[0] + xd[0]

  cycles = int(sum_hours/12) 
  print(cycles)
  number_of_days = round(sum_hours/24)

  if (cycles*12 == sum_hours):
    hours = sum_hours - (12 * cycles) + 12 
  else:
    hours = sum_hours - (12 * cycles)
  
  ex = str(AP[AP.index(x[1])-int(cycles%2)])
  days_later = ""

  if (number_of_days == 1 and ex == "AM"):
    days_later += "(next day)" 
  elif (number_of_days > 1):
    days_later += f"({str(number_of_days)} days later)"
      
  if (args):
    d = str(args[0]).capitalize()
    new_day = wd[(wd.index(d)+(int(number_of_days)%7))-len(wd)]
    new_time = str(hours) + ":" + str("{:02d}".format(minutes)) + " " + ex + ", " + new_day + " " + days_later

  else:
    new_time = str(hours) + ":" + str("{:02d}".format(minutes)) + " " + ex + " " + days_later
    
  new_time = new_time.rstrip()

  return new_time