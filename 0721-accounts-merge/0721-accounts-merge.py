from collections import defaultdict
from typing import List

class DSU:
    def __init__(self):
        self.parent = {}
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}
        
        # Step 1: Initialize DSU parents and map each email to its owner's name
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in dsu.parent:
                    dsu.parent[email] = email
                email_to_name[email] = name
                # Group all emails in the current account together
                dsu.union(email, first_email)
                
        # Step 2: Group emails by their representative parent component
        components = defaultdict(list)
        for email in dsu.parent:
            root = dsu.find(email)
            components[root].append(email)
            
        # Step 3: Format the final output: [Name, sorted_email1, sorted_email2, ...]
        merged_accounts = []
        for root, emails in components.items():
            name = email_to_name[root]
            merged_accounts.append([name] + sorted(emails))
            
        return merged_accounts


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna