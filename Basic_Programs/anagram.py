# Python function to check if two strings are anagrams 

def are_anagrams(str1, str2):
    # Convert strings to lowercase and remove non-alphabetic characters
    str1 = ''.join(c for c in str1.lower() if c.isalpha())
    str2 = ''.join(c for c in str2.lower() if c.isalpha())

    # Sort the characters in both strings
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Test the function
string1 = "Listen"
string2 = "Silent"
print("Are '{}' and '{}' anagrams?".format(string1, string2))
print(are_anagrams(string1, string2))
