from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Step 1: Initialize the graph and in-degree array
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # Step 2: Build the graph
        # prerequisites[i] = [course, prereq] -> prereq must be taken before course
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
            
        # Step 3: Add all courses with 0 in-degree (no prerequisites) to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        order = []
        
        # Step 4: Process the courses in the queue
        while queue:
            current = queue.popleft()
            order.append(current)
            
            # Decrease the in-degree for all neighboring courses
            for neighbor in adj_list[current]:
                in_degree[neighbor] -= 1
                # If a neighbor has no more prerequisites, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 5: If we successfully ordered all courses, return the path; 
        # otherwise, a cycle exists, making it impossible to finish.
        return order if len(order) == numCourses else []


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna