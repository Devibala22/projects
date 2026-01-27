class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int n=nums.length;
        int i=0;
        int j=0;
        int k=0;
        int[] arr1=new int[n];
        int[] arr2=new int[n];
        int[] res=new int[n];
        while(i<n){
            if(nums[i]%2==0){
                arr1[j]=nums[i];
                j++;
                  i++;
            }
            else{
                arr2[k]=nums[i];
                k++;
                  i++;
            }
            
        }
        System.arraycopy(arr1,0,res,0,j);
        System.arraycopy(arr2,0,res,j,k);
        return res;
    }
}
