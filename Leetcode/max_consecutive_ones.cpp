#include <iostream>
#include <vector>
#include <algorithm>

class Solution{
    public:
        int findMaxConsecutiveOnes(std::vector<int> &, int);
};

int Solution::findMaxConsecutiveOnes(std::vector<int> &nums, int sum){
    int counter {0}, global{0};
    for(auto &x : nums){
        if(x == 1){
            counter++;
        }
        else{
            global = std::max(counter, global);
            counter = 0;
        }   
    }
    return global;
}