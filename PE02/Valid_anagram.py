def isAnagram(s: str, t: str) -> bool:
    # If the lengths of the strings are different, they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Create a dictionary to count the occurrences of each character in s
    count = {}
    
    # Count characters in s
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Decrease the count based on characters in t
    for char in t:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False
        else:
            return False
    
    # If all counts are zero, then t is an anagram of s
    return all(value == 0 for value in count.values())

# Example 
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  
    print(isAnagram("rat", "car"))          