class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Given was an array of strings strs contains list of strings
        # our goal is to read each string and return the anagram taht contains the exact same characters as another string, order can be different
        # we can use a dictionary

        # in this case we use default dictionary because we are creating keys 

        # goal is to store the strings with the same keys

        #edge case
        if len(strs) == 0:
            return []

        #we create a dictionary 

        group= defaultdict(list)

        #going through each word in the string and making a key
        for word in strs:
            #key would be the sorted word of the strings
            key = "".join(sorted(word))
        
            #after creating the key we put it in the dictionary
            group[key].append(word)

        return list(group.values())

        


            


        








       
        