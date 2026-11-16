#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        // input: two strings
        //output: true if the two strings have the same characters or false
        // having two count variables for first and second string and initializing it
        int count1=0;
        int count2=0;
        //Edge case 1: if they have different letter's length then no need to look furhter
        if(s.length()!= t.length())
        {
            return false;
        }
        else if(s.length()==t.length())
        {

            std::unordered_map<char, int> count;
            //we start counting each character in the string
            //everytime it found a new character it will keep counting and adding to the table
        for(char c:s)
        {
            count[c]++;
        }
        for(char c:t)
        {
            //if we are checking the second string, we have to see whether the characters in the first string exist in the second string or not
            count[c]--;
            if (count[c]<0){
                return false;
            }
            
        }
        
        //Hashmap will help you keep accountable for the amount of characters that each string has
        //since the order doesn't matter, using unordered map would be faster
        return true;
    }

   
    }
};
