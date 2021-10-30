#imports
#variables
value1 = 'Susan'
value2 = 'n'
value3 = 'm'
value4 = 's'
value5 = 'cc'
value6 = 'm'
#functions
def build_user(value1, value2, value3, value4, value5, value6):
    '''Return a dictionary of information about a user'''
    user = {'name': value1, 'specialneeds': value2, 'bestsize': value3, 'lifestage': value4, 'social': value5, 'sex': value6}
    return user

#main
owner = build_user(value1, value2, value3, value4, value5, value6)
print(owner)