class Solution {
    public boolean isSameAfterReversals(int num) {
        String reversed = new StringBuilder(String.valueOf(num)).reverse().toString();
        int reversedInt = Integer.valueOf(reversed);

        reversed = new StringBuilder(String.valueOf(reversedInt)).reverse().toString();
        reversedInt = Integer.valueOf(reversed);

        return reversedInt == num;
    }
}