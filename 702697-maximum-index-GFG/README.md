# [Maximum Index](https://www.geeksforgeeks.org/problems/maximum-index3307/1?page=4&category=Arrays&sortBy=submissions)
## Medium
Given an array, arr[] of non-negative integers. The task is to return the maximum of j - i (i&lt;=j)&nbsp;subjected to the constraint of arr[i] &lt;= arr[j].
Examples:
Input: arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]Output: 6Explanation: In the given array arr[1] &lt; arr[7] satisfying the required condition (arr[i] &lt;= arr[j]) thus giving the maximum difference of j - i which is 7-1 = 6.
Input: arr[] = [18, 17]Output: 0Explanation: We can either take i and j as 0 and 0 or we cantake 1 and 1 both give the same result 0.
Input: arr[] = [10, 10, 10, 10]Output: 3Explanation: Since all elements are equal, any pair of indices will satisfy the condition arr[i] &lt;= arr[j]. The maximum difference is between j = 3 and i = 0, resulting in j - i = 3.
Constraints:1 ≤ arr.size() ≤ 1060 ≤ arr[i] ≤ 109