class Solution {
    public static void arrayTraversalReverse(int[] arr) {
        // Use StringBuilder for efficient string concatenation
        StringBuilder sb = new StringBuilder();
        
        for (int i = arr.length - 1; i >= 0; i--) {
            sb.append(arr[i]);
            // Add a space between numbers
            if (i > 0) {
                sb.append(" ");
            }
        }
        
        // Print everything in a single operation
        System.out.print(sb.toString());
    }
}
