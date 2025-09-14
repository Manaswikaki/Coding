class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l=nums.length;
        for(int i=0;i<l;i++){
            for(int j=0;j<l;j++){
                if(j==i){
                    continue;
                }
                if(nums[i]+nums[j] == target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
}