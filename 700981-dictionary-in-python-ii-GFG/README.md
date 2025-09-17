# [Dictionary in Python - II](https://www.geeksforgeeks.org/problems/dictionary-in-python-ii/1?page=1&category=python&sortBy=submissions)
## Easy
You are now familiar with the dictionary in Python. It's time to dive deeper into the dictionary in Python. How can you use a dictionary&nbsp;to store the frequency of elements in list L. Given below is one method:
for i in L:
     dict[i] = 0

for i in L:
     dict[i] += 1
Now, use this concept to solve a question. Given a list&nbsp;arr[], of&nbsp;positive integers, and an integer&nbsp;sum. The task is to check if any pair exists in the array whose sum is equal to the given&nbsp;sum. If such a pair exists return true, otherwise, return false.
Example:
Input: arr[] = [1, 2, 3, 3, 5], sum = 8 
Output: true
Explanation: Pair with sum 8 is present in the array which is (3, 5).
Input: arr[] = [3, 2, 5], sum = 6 
Output: false
Explanation: No such pair exists in the array.
Constraints:1 &lt;= arr.size() &lt;= 1041 &lt;= arr[i], sum &lt;= 104