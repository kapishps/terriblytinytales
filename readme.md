**Libraries Used**
 - urllib2 :- to get the contents of hosted file
 - re :- Regex Operations


----------


**Algorithm**

Since we have the whole input string given in start. I've used this approach for simplicity with all optimisations.
 - At first the file is cleaned to remove numbers and punctuations.
 - Then all the words are added to Trie and if a word is already present its frequency is increased. Time Complexity: O(total number of chars) , Space Complexity :  O(total number of chars)
 - Now a MinHeap of Max size N (given input) is used to keep N most frequent words at any time while travesing the Trie. Time Complexity: O(total number of words x logN) , Space Complexity :  O(N)


----------


![Sample Case N=6](https://photos.app.goo.gl/kisdDAZpJHau32Uv1)

****
