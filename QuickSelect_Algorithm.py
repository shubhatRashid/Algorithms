"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

"""
The approach is like quick sort but instead of sorting both the halves we sort only 
that half where our required element is located.
We divide the list using a pivot element and swap the elements which are smaller then 
pivot untill we get a list where each element on the left of pivot is less than pivot 
and on the right greater than pivot then we check if index of pivot is greater ,less
or equal to k and continue accordingly untill p == k
"""
def findKthLargest(nums, k):
    k = len (nums) - k # retrieve k from last

    def quickSelect(l, r):
        pivot, p = nums[r], l
        """
        pivot is the selected element for comparison
        p is the pointer which keeps track of the element
        to be swaped.
        """

        for i in range (l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p] # swapping
                p += 1
        nums[p], nums[r] = nums[r], nums[p] # swaping the pivot to its place

        if p == k:
            return nums[p]
        elif p < k:
            return quickSelect (p + 1, r)
        else:
            return quickSelect (l, p - 1)

    return quickSelect (0, len (nums) - 1)
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))