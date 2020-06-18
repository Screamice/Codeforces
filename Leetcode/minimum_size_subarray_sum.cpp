#include <iostream>
#include <vector>

class Solution{
    public:
        int minSubArrayLen(int s, std::vector<int> &nums);
};

int Solution::minSubArrayLen(int s, std::vector<int> &nums){
    for(auto i{0} ; i<nums.length() ; i++){
        if(s <= nums[i]+nums[i+1]){
            
        }
    }
}