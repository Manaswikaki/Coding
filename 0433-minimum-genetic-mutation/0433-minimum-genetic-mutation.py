from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # Convert bank to a set for O(1) fast lookup
        gene_bank = set(bank)
        
        # If the destination gene is not in the bank, it's an invalid mutation path
        if endGene not in gene_bank:
            return -1
        
        # Queue stores pairs of (current_gene, mutation_count)
        queue = deque([(startGene, 0)])
        
        # Track visited genes to prevent infinite loops
        visited = {startGene}
        
        # Available character options for mutation
        choices = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # If we reached the target gene, return the step count
            if current_gene == endGene:
                return mutations
            
            # Generate all possible single-character mutations
            for i in range(len(current_gene)):
                for char in choices:
                    if char != current_gene[i]:
                        # Create the new mutated gene string
                        mutated = current_gene[:i] + char + current_gene[i+1:]
                        
                        # Check if it's a valid next step
                        if mutated in gene_bank and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, mutations + 1))
                            
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna