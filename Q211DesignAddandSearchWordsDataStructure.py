# 211. Design Add and Search Words Data Structure

# Medium

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.


class WordDictionary:

    def __init__(self):
        self.store = []

    def addWord(self, word: str) -> None:
        self.store.append(word)

    def search(self, word: str) -> bool:
        for w in self.store:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':
                    i += 1
                else:
                    break
            if i == len(w):
                return True
        return False
    
# Brute Force
# We use a list to store the words. 
# When adding a word, we simply append it to the list.
# When searching, we iterate through the list and check if the word matches, considering '.' as a wildcard. 
# We check the length first to avoid unnecessary comparisons.
# Then we compare each character, allowing for '.' to match any character.
# Break the loop if a character doesn't match and continue to the next word.
# if the entire word matches, we return True. If no matches are found after checking all words, we return False.
# This approach is simple but may not be efficient for large datasets.
# Time Complexity: O(n * m) for search, where n is the number of words and m is the length of the word being searched.
# Space Complexity: O(n * m) for storing the words, where n is the number of words and m is the average length of the words.



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c= word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)


# Trie Implementation
# We can implement a Trie (prefix tree) to store the words.
# Each node in the Trie will have a dictionary to store its children and a boolean flag to indicate if it marks the end of a word.
# For the addWord operation, we traverse the Trie according to the characters of the word, creating new nodes as necessary.
# For the search operation, we use a depth-first search (DFS) approach to handle the '.' wildcard.
# If we encounter a '.', we recursively search all possible children nodes.
# Else, we continue traversing the Trie according to the characters of the word.
# If we reach the end of the word, we check if the current node marks the end of a word.
# Time Complexity:
# The time complexity for addWord is O(1), where m is the length of the word being added. 
# The time complexity for search is O(n * m) in the worst case, where n is the number of words in the Trie and m is the length of the word being searched, due to the potential branching caused by '.' wildcards.
# Space Complexity: O(n * m) for storing the words in the Trie, where n is the number of words and m is the average length of the words.
