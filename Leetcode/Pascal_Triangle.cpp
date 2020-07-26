#include <iostream>
#include <vector>

class Solution {
    public:
        std::vector<int> GetRow(int idx);
        long long int factorial(int numb);
};

std::vector<int> Solution::GetRow(int idx) {
    std::vector<int> ans(idx+1, 0);
    for(int i=0 ; i<ans.size() ; i++){
        ans[i] = (int)(factorial(idx) / (factorial(i) * factorial(idx-i)));
    }

    return ans;
}

long long int Solution::factorial(int numb) {
    return (numb==0 || numb==1)? 1 : numb*factorial(numb-1);
}

int main() {
    std::vector<int> numbs;

    Solution sol;
    numbs = sol.GetRow(21);

    for(auto &K : numbs){
        std::cout << K << " ~ ";
    }

    std::cout <<  std::endl;
}