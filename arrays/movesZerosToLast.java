public static void moveZeroesToLast(int[] nums) {

        if (nums.length == 1) {
            System.out.println(nums);
        }
        int r = 1, l = 0;
        while(r < nums.length){
            if(nums[l] == 0){
                l++;
                r++;
            }
            else if(nums[r] != 0){
                r++;
            }
            else{
                int temp = nums[r];
                nums[r] = nums[l];
                nums[l] = temp; 

            }
        }

        for(int index = 0;index < nums.length;index++){
            System.out.println(nums[index]);
        }

    }
