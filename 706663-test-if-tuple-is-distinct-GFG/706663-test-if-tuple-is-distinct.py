#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

########### Write your code above ###############
# Read a line of input as space-separated integers and convert to a tuple
# Check if all elements are unique
if len(arr) == len(set(arr)):
    print("True")
else:
    print("False")