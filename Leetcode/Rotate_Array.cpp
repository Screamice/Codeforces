#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

class Solution {
    public:
        void Rotate(std::vector<int> &nums, int k);
};

/**
    *   Solución trivial O(n x k)
    *  
    *   void Solution::Rotate(std::vector<int> &nums, int k) {
    *       k %= nums.size();
    *       int aux, prev;
    *       for(int j=0; j<k ; j++){
    *           prev = nums[nums.size() - 1];
    *           for(int i=0 ; i<nums.size() ; i++){
    *               aux = nums[i];
    *               nums[i] = prev;
    *               prev = aux;
    *           }
    *       }
    *   }
*/

/**
        void Solution::Rotate(std::vector<int> &nums, int k){
            k %= nums.size();
            int count{0};
            for(int i=0 ; count<nums.size() ; i++){
                int current = i;
                int prev = nums[i];
                do{
                    int next = (k + current)%nums.size();
                    int temp = nums[next];
                    
                    nums[next] = prev;
                    prev = temp;

                    current = next;
                    count++;
                }
                while(i != current);
            }
        }
*/

void Solution::Rotate(std::vector<int> &nums, int k){
    k %= nums.size();
    std::reverse(nums.begin(), nums.end());
    std::reverse(nums.begin(), nums.begin()+k);
    std::reverse(nums.begin()+k, nums.end());
}

int main() {
    std::vector<int> nums = {1,2,3,4,5,6};

    Solution inst;
    inst.Rotate(nums, 10);

    for(auto idx: nums){
        std::cout << idx << " ";
    }
    std::cout << std::endl;
}