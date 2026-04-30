import java.util.ArrayList;

class Solution {
    // Function to return an ArrayList with exact result and formatted result
    static ArrayList<Float> divisionWithPrecision(float a, float b) {
        ArrayList<Float> result = new ArrayList<>();
        
        // 1. Calculate the exact result
        float exactResult = a / b;
        
        // 2. Round the result to three decimal places
        // We multiply by 1000, round to the nearest integer, then divide by 1000.0f
        float roundedResult = Math.round(exactResult * 1000.0f) / 1000.0f;
        
        // Add both to the list
        result.add(exactResult);
        result.add(roundedResult);
        
        return result;
    }
}
