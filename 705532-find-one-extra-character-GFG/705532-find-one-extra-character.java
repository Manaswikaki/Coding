class Solution {
    public static char extraChar(String s1, String s2) {
        int res = 0;

        // XOR all characters in s1
        for (int i = 0; i < s1.length(); i++) {
            res ^= s1.charAt(i);
        }

        // XOR all characters in s2
        for (int i = 0; i < s2.length(); i++) {
            res ^= s2.charAt(i);
        }

        // The remaining value is the extra character
        return (char) res;
    }
}
