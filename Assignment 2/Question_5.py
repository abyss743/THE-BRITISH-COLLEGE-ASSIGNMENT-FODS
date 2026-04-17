'''
Function to sort student names in reverse alphabetical order.
'''

def rev_names(names):
    return sorted(names, reverse=True)

students = ["Alice", "Bob", "Charlie", "Diana"]
print("Reverse order:", rev_names(students))
