def strStr(haystack: str, needle: str) -> int:
    # If needle is an empty string, return 0
    if not needle:
        return 0
    
    # Get the lengths of haystack and needle
    haystack_length = len(haystack)
    needle_length = len(needle)
    
    # If needle is longer than haystack, it cannot be found
    if needle_length > haystack_length:
        return -1
    
    # Iterate through the haystack
    for i in range(haystack_length - needle_length + 1):
        # Check if the substring matches the needle
        if haystack[i:i + needle_length] == needle:
            return i  # Return the starting index of the match
    
    return -1  

# Example
if __name__ == "__main__":
    print(strStr("hello", "ll"))  
    print(strStr("aaaaa", "bba"))  
    print(strStr("hello", ""))     