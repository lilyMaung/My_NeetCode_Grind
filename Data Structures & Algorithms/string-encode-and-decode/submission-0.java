class Solution {
    /**
    Encoding will take a list of strings such as ["Hello","world"]
    Put them and squish all the strings into one single string or line
    **/

    public String encode(List<String> strs) 
    {
        String myEncode ="";
        //Going through each word in a string list
        for(int i=0; i<strs.size();i++)
        {
            //storing each word in a string called mystring
            String myString=strs.get(i);

            myEncode +=    myString.length()+ "#" + myString;
            // //then breaking the word into characters and storing in character arraylist
            // char[] myCharacter= new char[myString.length()];
            // //looping through the character array list, character by character
            // for(char c: myCharacter)
            // {
            //     //i am going to put the length of a word infront and some character such as "#" to encode
            //     c += valueOf(myCharacter.length)+c;
            // }
            System.out.println(myString);
        }
        return myEncode;

    }
    /**
        Decoding takes that one string encoding has created and turn it back into the original string list
    **/


    public List<String> decode(String str) 
    {
        //decoding for example 12#helloworld76
        
        int i=0;
        //creating a list of strings to put when you read the encode

        List<String> myDecode = new ArrayList<>();
       
        while(i<str.length())
        {
            //finding the index of when we find "#"
             // finds "#" starting FROM position i
                int start = str.indexOf("#",i);
              //reading the number before the "#"
                int length= Integer.parseInt(str.substring(i, start));
                myDecode.add(str.substring(start+1, start+1+length));
            
                i=start+1+length;
        
        }

         return myDecode;

    }
}
