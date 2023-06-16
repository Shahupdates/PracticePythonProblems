"""
Find the Maximum XOR of Two Numbers in an Array

Write a program that takes an array of integers as input and finds the maximum XOR value of any two numbers in the array.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if bit not in node.children:
                node.children[bit] = TrieNode()

            node = node.children[bit]

        node.value = num

    def find_max_xor(self, num):
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit

            if opposite_bit in node.children:
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]

        return num ^ node.value

def find_max_xor(nums):
    trie = Trie()

    for num in nums:
        trie.insert(num)

    max_xor = 0

    for num in nums:
        xor = trie.find_max_xor(num)
        max_xor = max(max_xor, xor)

    return max_xor

# Take input from the user
nums = list(map(int, input("Enter the array of integers (separated by spaces): ").split()))

# Find the maximum XOR value
max_xor = find_max_xor(nums)

# Print the result
print("The maximum XOR value is", max_xor)
