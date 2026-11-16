#include<unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        //Understanding the problem
        //input is the array
        //output will be the two indices of the two array numbers whose values' sum is target
        //constraints: 2<= nums.length <=1000
        //-10,000,000 <= nums[i] <= 10,000,000
        //-10,000,000 <= target <= 10,000,000
        std::unordered_map<int, int> myHashMap;
            int hashnumber;
            int complement;
        //we will iterate through an array and put it in the hashmap

        for (int i=0; i<nums.size(); i++)
        {
            hashnumber=nums[i];
            complement= target - hashnumber;
        
            if (myHashMap.count(complement))
            {
               return {myHashMap[complement],i};
            }
            myHashMap[hashnumber] = i;
        }
        //after iterating, now it's time to find the sums
        return {};
    }
};