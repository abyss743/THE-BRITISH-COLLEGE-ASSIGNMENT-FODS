'''
Function to search country and return index or Not Found in List.
'''

def find_country(clist, target):
    if target in clist:
        return clist.index(target)
    return "Not Found in List"

countries = ["Nepal", "India", "China", "USA"]
print(find_country(countries, "Nepal"))
print(find_country(countries, "Japan"))
