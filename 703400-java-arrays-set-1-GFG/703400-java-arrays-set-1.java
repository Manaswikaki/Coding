class Solution {
    public String average(int arr[]) {
        if (arr == null || arr.length == 0) {
            // Handle edge case if needed; here we return "0.00"
            return "0.00";
        }

        long sum = 0; // use long to avoid potential overflow, though constraints are small
        for (int v : arr) {
            sum += v;
        }

        double avg = (double) sum / arr.length;
        // Format to two decimal places
        return String.format("%.2f", avg);
    }
}