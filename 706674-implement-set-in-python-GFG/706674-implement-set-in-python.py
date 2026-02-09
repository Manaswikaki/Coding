# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    s.add(element)

# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    # Use discard to avoid KeyError if element not present
    s.discard(element)

# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    return sum(s)