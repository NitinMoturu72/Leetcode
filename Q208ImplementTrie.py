# 208. Implement Trie (Prefix Tree)

# Medium

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  
        cur.endOfWord = True      

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True     
    
# Prefix Tree HashMap Implementation
# We can implement a Trie using a HashMap (or dictionary in Python) to store the children of each node and a flag to indicate the end of a word. 
# Each node will have a dictionary where the keys are characters and the values are the corresponding child nodes. 
# This allows for efficient insertion and search operations.
# For the insert operation, we traverse the Trie according to the characters of the word, creating new nodes as necessary.
# For the search operation, we traverse the Trie according to the characters of the word and check if we reach a node that marks the end of a word.
# For the startsWith operation, we traverse the Trie according to the characters of the prefix and check if we reach a node that marks the end of a word.
# Time Complexity:
# The time complexity for insert, search, and startsWith operations is O(m), where m is the length of the word or prefix being inserted or searched. This is because we need to traverse the Trie for each character in the word or prefix.
# Space Complexity:
# The space complexity is O(n * m), where n is the number of words inserted into the Trie and m is the average length of the words. Each node in the Trie can have up to 26 children (for lowercase English letters), and we may need to create new nodes for each character in the words being inserted.