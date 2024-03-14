# Valid Parentheses python prog
def is_valid(s):
    stack = []
    # Define a dictionary to store the mappings of opening and closing parentheses
    mappings = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mappings.values():
            # If the character is an opening parenthesis, push it onto the stack
            stack.append(char)
        elif char in mappings.keys():
            # If the character is a closing parenthesis, check if the stack is empty
            # If it's empty or the top of the stack doesn't match the expected opening parenthesis, return False
            if not stack or stack.pop() != mappings[char]:
                return False
        else:
            # If the character is neither an opening nor a closing parenthesis, skip it
            continue
    
    # After iterating through all characters, if the stack is empty, the parentheses are valid
    return not stack

# Example usage:
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"

print("s1 is valid:", is_valid(s1))
print("s2 is valid:", is_valid(s2))
print("s3 is valid:", is_valid(s3))
print("s4 is valid:", is_valid(s4))
print("s5 is valid:", is_valid(s5))
