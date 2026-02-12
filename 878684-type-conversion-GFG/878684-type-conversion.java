import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        double d = sc.nextDouble();
        // Typecast and print
        int result = (int) d; // Typecast double to int (truncates decimal part)
        System.out.println(result);
        
    }
}
