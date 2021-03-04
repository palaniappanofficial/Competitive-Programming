def number_to_string(string):
    dictionary={
        '0':'Zero',
        '1':'One',
        '2':'Two',
        '3':'Three',
        '4':'Four',
        '5':'Five'
    }
    return dictionary.get(string,"Nothing")
a=number_to_string('0')
print(a)
a=number_to_string('8')
print(a)
a=number_to_string('2')
print(a)
a=number_to_string('3')
print(a)