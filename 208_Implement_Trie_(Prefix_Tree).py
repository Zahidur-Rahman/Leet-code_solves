class TrieNode:
    def __init__(self):
        self.children = {}  # A dictionary to store child nodes
        self.is_end_of_word = False  # Indicates if the node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if it doesn't exist
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """Search for a word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If character is not found, word doesn't exist
            node = node.children[char]
        return node.is_end_of_word  # Return True only if it's the end of a word

    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # If character is not found, no word has this prefix
            node = node.children[char]
        return True  # If we traverse the prefix successfully, return True


