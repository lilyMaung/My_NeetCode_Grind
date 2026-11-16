class Solution {
    public int[] topKFrequent(int[] nums, int k) 
    {
        //INPUT-ARRAY OF NUMBERS AND K AS HOW MANY FREQUENT NUMBERS
        //OUTPUT- DEPENDING ON K, IT WILL ARRANGE FROM MOST TO LEAST FREQUENCT NUMBERS

        //building an unordered hashmap
        HashMap<Integer, Integer> myMap=new HashMap<Integer, Integer>();

        ArrayList<Integer> myArray = new ArrayList<Integer>();
        for(int i=0; i<nums.length;i++)
        {
            //k has to be at least one
            
                if(!myMap.containsKey(nums[i]))
                {
                   // myArray[i]=indexOf(nums[i]);
                    //String key=str(myArray[i]);
                    myMap.put(nums[i],1);
                }
                else
                {

                    //get will get the index of that key and increment it by 1
                    myMap.put(nums[i],myMap.get(nums[i])+1);

                }
                //now we has all keys and values in the hashmap
                //since we want to sort my keys, map itself cannot sort itself 
                //so we gonna put the keys of the map as an array list then sort with the keys
               
        }
             List<Integer> myList =new ArrayList<>(myMap.keySet());

                //we gonna start sorting the array and comparing
                myList.sort((a,b) -> myMap.get(b) - myMap.get(a)); 
                
             //now we get the k numbers
                int[] myK = new int[k];
                // Step 3: Take top k element
            for (int i = 0; i < k; i++) 
            {
                myK[i] = myList.get(i);
            }
          return myK;
    }
   
   
}
