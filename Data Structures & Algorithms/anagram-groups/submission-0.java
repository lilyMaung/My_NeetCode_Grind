class Solution {
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        //key is the character and value is words that match
        HashMap<String, List<String>> myStringMap = new HashMap<>();

        //we will go through each string
        for(String s:strs)
        {
        //luckily we only have 26 alphabets
        int[] count=new int[26];
        for(char c:s.toCharArray()){
            count[c - 'a']++;
        }

        //turning count into key
        String key=Arrays.toString(count);

        if(!myStringMap.containsKey(key)){
            myStringMap.put(key, new ArrayList<>());
        }
        myStringMap.get(key).add(s);
        }
        return new ArrayList<>(myStringMap.values());
        
    } 
    
}
