#include <iostream>
#include <vector>
#include <algorithm>

class Solution{
    public:
        int minSubArrayLen(int s, std::vector<int> &nums);
};

int Solution::minSubArrayLen(int s, std::vector<int> &nums){

    int size = nums.size();
    if(!size || size == NULL){ return 0; }

    int ans = INT16_MAX, left{0}, sum{0};

    for(auto i=0 ; i<size ; i++){
        sum += nums[i];
        while(sum >= s){
            ans = std::min(ans, i+1-left);
            sum -= nums[left++];
        }
    }

    return (ans != INT64_MAX)? ans : 0;
}

int main(){
    Solution sol;
    std::vector<int> array = {2,3,1,2,4,3};
    std::cout << sol.minSubArrayLen(7, array) << std::endl;
}