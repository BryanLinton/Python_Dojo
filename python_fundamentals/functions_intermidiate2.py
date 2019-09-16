def update_val():
    x = [ [5,2,3], [10,8,9] ] 
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [ {'x': 10, 'y': 20} ]

    x [1][0] = 15
    students[0]['lastname'] = 'Bryant'
    sports_directory['soccer'][0] = 'Andres' 
    z[0]['y'] = 30
    return x, students, sports_directory, z

print(update_val())


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
  for dicts in some_list:
   disp_str = ''
   for k,v in dicts.items():
    disp_str+= k +' - '+ v + ', '
   print(disp_str[:len(disp_str) - 2])
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dicts in some_list:
        print(dicts[key_name])
print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
  for key in some_dict.keys():
    print(f"{len(some_dict[key])} {key.upper()}")
    for item in some_dict[key]:
      print(item)
    # this prints a new line
    print('\n')

print_info(dojo)
