#imports
from csv import DictReader

#open file in read mode
with open('csv.dogs100dictprep.csv', 'r') as read_obj:
    #pass file object to DictReader(), get DictReader object
    dict_reader = DictReader(read_obj)
    #get a list of dictionaries from dict_reader
    list_of_dict = list(dict_reader)
    print(list_of_dict)

