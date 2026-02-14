import math
class Solution:
    def switchCase(self, choice, arr):
        # Using if-elif-else for switch-case functionality [1]
        if choice == 1:
            # Area of circle: π * r^2
            # Assuming arr[0] is radius
            return (math.pi) * (arr[0]**2) # Using math.pi for better precision
        elif choice == 2:
            # Area of rectangle: length * breadth
            # Assuming arr[0] is length and arr[1] is breadth
            return arr[0] * arr[1]
        else:
            # Default case
            return 0