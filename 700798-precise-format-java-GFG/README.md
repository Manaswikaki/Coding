# [Precise Format - Java](https://www.geeksforgeeks.org/problems/precise-fomat-java/1?page=1&category=Java&sortBy=submissions)
## Easy
In many cases, dividing two numbers can contain an excessive number of decimal places. In this problem, your task is to compute the division of two floating-point numbers and format the result to a specific precision.
You are given two floating-point numbers a and b. Your task is to:

Output the exact result of a / b.
Format and output the result of a / b rounded to three decimal places.

You may use&nbsp;System.out.format() to format the output.
You need to return an ArrayList with two values:

The first value is the exact result of a / b.
The second value is the result rounded to three decimal places.

Examples:
Input: a = 5.43, b = 2.653
Output: [2.0467393, 2.047]Explanation: a/b and decimal precision of a/b up to 3 places after the decimal point are given.
Input: a = 3.25, b = 2.5Output: [1.3, 1.300]Explanation: a/b and decimal precision of a/b up to 3 places after the decimal point are given.
Input: a = 10.0, b = 4.0Output: [2.5, 2.500]Explanation: Division of a by b gives the exact result 2.5 and the formatted result 2.500.
Constraints:1 &lt;= a, b &lt;= 109