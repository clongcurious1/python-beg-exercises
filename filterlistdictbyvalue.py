import time

from csv import DictReader

value1 = 'Samantha'
value2 = 'n'
value3 = 'l'
value4 = 's'
value5 = 'sg'
value6 = 'f'

#to print 100dogs as list of dictionaries
with open('csv.dogs100dictprep.csv', 'r') as read_obj:
    #pass file object to DictReader(), get DictReader object
    dict_reader = DictReader(read_obj)
    #get a list of dictionaries from dict_reader
    list_of_dict = list(dict_reader)
    #print(list_of_dict)

#start matching against user prerequisites
#rename list_of_dict *you can rename a variable anywhere in the program
petstoadopt = list_of_dict
print('\nHere is the full list of available pets:\n')
print(petstoadopt)
time.sleep(2)

#Round 1 Pet Match: Special Needs (value2)
#use a dictionary comprehension to match specialneeds:value2
print ("\nFILTER: Match pets against user's 'specialneeds' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value2)] #value you are matching against
newList1 = [d for d in petstoadopt if d['specialneeds'] in keyValList]
print(newList1)
time.sleep(2)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance() to count # of dicts in new list
result1 = len([ele for ele in newList1 if isinstance(ele, dict)])
print("\nSPECIAL NEEDS: The number of matching pets is " + str(result1))
time.sleep(3)

#Round 2 Pet Match: Best Size (value3)
#use a dictionary comprehension to match bestsize:value3
print ("\nFILTER: Match pets against user's 'bestsize' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value3)] #value you are matching against
newList2 = [d for d in newList1 if d['bestsize'] in keyValList]
print(newList2)
time.sleep(2)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result2 = len([ele for ele in newList2 if isinstance(ele, dict)])
print("\nSpecial Needs + Best Size: NEW number of matching pets is " + str(result2))
time.sleep(2)

#Round 3 Pet Match: Life Stage (value4)
#use a dictionary comprehension to match lifestage:value4
print ("\nFILTER: Match pets against user's 'lifestage' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value4)] #value you are matching against
newList3 = [d for d in newList2 if d['lifestage'] in keyValList]
print(newList3)
time.sleep(2)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result3 = len([ele for ele in newList3 if isinstance(ele, dict)])
print("\nSpecial Needs, Best Size, Life Stage: NEW number of matching pets is " + str(result3))
time.sleep(2)

#Round 4 Pet Match: Social Needs (value5)
#use a dictionary comprehension to match social:value5
print ("\nFILTER: Match pets against user's 'social' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value5)] #value you are matching against
newList4 = [d for d in newList3 if d['social'] in keyValList]
print(newList4)
time.sleep(2)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result4 = len([ele for ele in newList4 if isinstance(ele, dict)])
print("\nSpecial Needs, Best Size, Life Stage, Social Needs: Number of matching pets is " + str(result4))
time.sleep(2)

#Commented this out lines 87-101 because when the file is being read
#the dict.reader is printing the value of key: sex with an extra space
# extra space "f " or "m " inside quotes is crashing the program
#Round 5 Pet Match: Sex (value6)
#use a dictionary comprehension to match sex:value6
#print ("\nFILTER: Match pets against user's 'sex' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
#keyValList = [str(value6)] #value you are matching against
#newList5 = [d for d in newList4 if d['sex'] in keyValList]
#print(newList5)
#time.sleep(2)

##How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
#result5 = len([ele for ele in newList5 if isinstance(ele, dict)])
#print("\nSpecial Needs, Best Size, Life Stage, Social Needs, Sex: Number of matching pets is " + str(result5))
#time.sleep(2)