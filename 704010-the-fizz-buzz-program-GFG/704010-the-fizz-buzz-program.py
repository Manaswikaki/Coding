class Solution:
    def fizzBuzz(self, number):
        # Check divisibility by both 3 and 5 first
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # Check divisibility by 3
        elif number % 3 == 0:
            print("Fizz")
        # Check divisibility by 5
        elif number % 5 == 0:
            print("Buzz")
        # If not divisible by 3 or 5, print the number
        else:
            print(number)
