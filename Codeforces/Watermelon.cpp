#include <iostream>

class Solution {
    public:
        std::string DivideWatermelon(int weight);
};

std::string Solution::DivideWatermelon(int weight) {
    auto tail = weight%2;
    if(tail || weight==2){
        return "NO";
    }
    else{
        return "YES";
    }
}

int main() {
    int weight {0};
    std::cin >> weight;

    Solution obj;
    std::string ans = obj.DivideWatermelon(weight);

    std::cout << ans << std::endl;
}