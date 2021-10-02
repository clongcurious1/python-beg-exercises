#print activity list by day
day = input("What day of the week is it?\n")
if day == 'Monday' or day == 'Wednesday':
    alarm = '7.30am'
    carpool = True
    coding_class = True
    gym = False
elif day == 'Tuesday' or day == 'Thursday':
    alarm = '7.30am'
    carpool = False
    coding_class = False
    gym = True
elif day == 'Friday':
    alarm = '6.30am'
    carpool = True
    coding_class = False
    gym = False
else:
    alarm = 'OFF'
    carpool = False
    coding_class = False
    gym = True
print("Today's To Do List:")
print("Alarm:", alarm)
print("Carpool:", carpool)
print("Coding Class:", coding_class)
print("Gym:", gym)
print("Have a GREAT day!")