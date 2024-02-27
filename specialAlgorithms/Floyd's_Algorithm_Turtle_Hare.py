"""
Turtle Hare Algorithm:
    In this algorithm , we treat the array as a linked list with each
    entry in the array as a pointer to the next element in the array

"""


def findDuplicate(nums):
    slow = 0 #turtle
    fast = 0 #Hare

    while True: #detect the cycle
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0 #second turtle
    while True: #confirm the cycle
        slow2 = nums[slow2]
        slow = nums[slow]
        if slow2 == slow:
            return slow

