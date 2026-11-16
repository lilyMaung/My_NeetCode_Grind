class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating a hash map
        count ={}
        #then we gonna put our frequencies as keys
        #in this case, we gonna loop through our array and put the counts or frequencies as keys
        for num in nums:
            #if it's already in the map, it will increment by one, if not then it will come as zero 
            count[num] = count.get(num, 0) +1

        #now we got the keys with counts
        #we gonna do bucket sort, which means we gonna put all the numbers with the same frequency
        #this will create each frequency list for each count

        freq = [[] for _ in range(len(nums)+1)]

        #count has numbers and counts in the map
        for num, c in count.items():
            #in this frequency count, this wiill be these numbers
            freq[c].append(num)
        
        # now frequncy has its count and numbers

        #now we need to go through in descending order in order to find the most k frequent numbers
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result


            

        
        







      