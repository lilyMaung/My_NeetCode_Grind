class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
     
    std::set<int> myDuppy;
     for(int num: nums){
        if(myDuppy.find(num)!=myDuppy.end()){
            return true;
        }
        myDuppy.insert(num);
     }
     return false;




    }
};