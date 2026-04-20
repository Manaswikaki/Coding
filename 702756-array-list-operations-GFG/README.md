# [ArrayList Operations](https://www.geeksforgeeks.org/problems/arraylist-operations/1?page=7&category=Java&sortBy=submissions)
## Easy
In this question we will be implementing q&nbsp;number&nbsp;operations on ArrayList. There will be different type of queries.A query can be of&nbsp;five&nbsp;types:1. a x (Adds an element x to the ArrayList A&nbsp;at the end)2. b (Sorts the ArrayList A in ascending order)3. c (Reverses the ArrayList A)4. d (prints the size of the ArrayList)5. e (Sorts the ArrayList A in descending order)6. f&nbsp;&nbsp;(prints space separated values of the ArrayList)
Examples:
Input: q = 6, queries = "a 4 a 6 a 7 b c e"Output: 7 6 4Explanation:
There are six queries.
Queries are performed in this order
1. a 4 {ArrayList has 4}
2. a 7 {ArrayList has 4,7}
3. a 6 {ArrayList has 4,7,6}
4. b {sorts the ArrayList in ascending order,
&nbsp;     ArrayList now is 4 6 7}
5. c {reverse the ArrayList to 7 6 4}
6. e {prints the elements of ArrayList i.e. 7 6 4}
Input: q = 4, queries = "a 55 a 11 d e"Output: 2 55 11
Explanation :
There are four queries.
Queries are performed in this order
1. a 55 {ArrayList has 55}
2. a 11 {ArrayList has 55,11}
3. d {prints the size of the ArrayList i.e. 2}
4. e {prints the elements of ArrayList i.e. 55 11}
Constraints:1&lt;=Q&lt;=100