import java.util.*;

class Solution {
    // 1. Adds an element x to the ArrayList A at the end
    public static void add_to_ArrayList(ArrayList<Integer> A, int x) {
        A.add(x);
    }

    // 2. Sorts the ArrayList A in ascending order
    public static void sort_ArrayList_Asc(ArrayList<Integer> A) {
        Collections.sort(A);
    }

    // 3. Reverses the ArrayList A
    public static void reverse_ArrayList(ArrayList<Integer> A) {
        Collections.reverse(A);
    }

    // 4. Returns the size of the ArrayList
    public static int size_Of_ArrayList(ArrayList<Integer> A) {
        return A.size();
    }

    // 5. Sorts the ArrayList A in descending order
    public static void sort_ArrayList_Desc(ArrayList<Integer> A) {
        Collections.sort(A, Collections.reverseOrder());
    }

    // 6. Prints space-separated values of the ArrayList
    public static void print_ArrayList(ArrayList<Integer> A) {
        for (int i = 0; i < A.size(); i++) {
            System.out.print(A.get(i) + " ");
        }
    }
}
