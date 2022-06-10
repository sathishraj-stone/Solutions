"""1. For a given string input, make lists for digits and letters:
I/P - "2022: Dell EMC Bangalore Karnataka-560048"

output should have two lists, one should have list of digits present in the above string and other should have numbers."""

input_string = "2022: Dell EMC Bangalore Karnataka-560048"
number_list = []
letters_list = []

for item in input_string:
    if item.isnumeric():
        number_list.append(item)
    elif item.isalpha():
        letters_list.append(item)
print(number_list, letters_list)


"""2. Write a program to construct a dictionary like {'State': [cities,...],} from the given input

I/P: cities = {'Bangalore': 'Karnataka', 'Kannur': 'Kerala', 'Mysore': 'Karnataka', 'Salem': 'Tamil Nadu',
               'Mangalore': 'Karnataka', 'Mumbai': 'Maharastra', 'Coimbatore': 'Tamil Nadu', 'Udupi': 'Karnataka',
               'Pune': 'Maharastra'}
O/P: {'Karnataka': ['Bangalore', 'Mysore', 'Udupi', 'Mangalore'], 'Kerala': ['Kannur', ...], ,,,}"""
cities = {'Bangalore': 'Karnataka', 'Kannur': 'Kerala', 'Mysore': 'Karnataka', 'Salem': 'Tamil Nadu',
               'Mangalore': 'Karnataka', 'Mumbai': 'Maharastra', 'Coimbatore': 'Tamil Nadu', 'Udupi': 'Karnataka',
               'Pune': 'Maharastra'}

values = []
for key, value in cities.items():
    values.append(value)
state_city = dict()
for item in set(values):
    city_list = []
    for key in cities:
        if cities[key] == item:
            city_list.append(key)
    state_city.update({item: city_list})
print(state_city)


"""3. Given a sentence, there is no space between different words and the first letter of every word is in uppercase. Write
a program to print the output in the following format

1. Convert the uppercase letters to lowercase
2. Single space between each word

Example I/P -
ViratKohliIsTheLeadingRunScorerInIpl2022

Expected O/P - virat kohli is the leading run scorer in the ipl2022"""
input_string = "ViratKohliIsTheLeadingRunScorerInIpl2022"
output_string = ""
for index, letter in enumerate(input_string):
    if index == 0:
        output_string += letter.lower()
    elif letter.islower():
        output_string += letter
    elif letter.isupper():
        output_string += " " + letter.lower()
    else:
        output_string += letter
print(output_string)
