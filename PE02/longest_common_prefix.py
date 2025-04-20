def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the initial prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Update the prefix until it matches the beginning of the current string
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]  # Remove the last character from the prefix
            
        # If the prefix becomes empty, there is no common prefix
        if not prefix:
            break
    
    return prefix

# Example usage:
if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))  
    print(longestCommonPrefix(["dog", "racecar", "car"]))     