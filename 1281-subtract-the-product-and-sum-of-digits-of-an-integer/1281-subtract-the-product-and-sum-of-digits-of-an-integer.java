class Solution {
    public int subtractProductAndSum(int n) {
        int product = 1, add = 0, temp = n;
        while(temp > 0){
            add += temp%10;
            product *= temp%10;
            temp /= 10;
        }

        return product-add;
    }
}