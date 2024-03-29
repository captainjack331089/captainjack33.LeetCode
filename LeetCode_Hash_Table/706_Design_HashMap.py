"""
706. Design HashMap
Category: Hash Table
Difficulty: Easy
"""
"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here
        """
        self.array = [-1] * 1000000

    def put(self,key,value):
        """
        value will always be negative
        """
        self.array[key] = value

    def get(self,key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.array[key]

    def remove(self,key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.array[key] = -1

if __name__ == "__main__":
    myArray = MyHashMap()
    myArray.put(1,1)
    print(myArray.get(1))
    myArray.put(1,2)
    print(myArray.get(1))
    myArray.put(3,5)
    print(myArray.get(3))
    myArray.remove(3)
    print(myArray.get(3))
