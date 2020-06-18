#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
    public:
        int findMaxConsecutiveOnes(vector<int> &nums);
};

int Solution::findMaxConsecutiveOnes(vector<int> &nums){
    int counter {0}, global{0};
    for(auto &x : nums){
        if(x == 1){
            counter++;
        }
        else{
            global = max(counter, global);
            counter = 0;
        }   
    }
    return global;
}

int main(void){
    sol = Solution();
    sol.findMaxConsecu
}