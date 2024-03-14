'''

To find the product of array except self, you can use the following approach:

Initialize two arrays left_product and right_product, where left_product[i] represents the product of all elements to the left of nums[i], and right_product[i] represents the product of all elements to the right of nums[i].
Iterate through the input array nums from left to right and compute the left_product array.
Iterate through the input array nums from right to left and compute the right_product array.
Finally, compute the result array by multiplying corresponding elements from left_product and right_product
'''

def product_except_self(nums):
    n = len(nums)
    left_product = [1] * n
    right_product = [1] * n
    result = [1] * n
    
    # Compute left_product
    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]
    
    # Compute right_product
    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]
    
    # Compute result array
    for i in range(n):
        result[i] = left_product[i] * right_product[i]
    
    return result

# Example usage:
nums = [1, 2, 3, 4]
print("Product of array except self:", product_except_self(nums))
