# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# check if both or one list is empty, if both are empty return an Node head
# if one is empty and the other isn't, return the head of the non-empty list
# make an empty node variabke called fake_head to be the head of the merged linked list that will be returned
# make a variable called tail that is set to the fake_head
# make two variables, current_1 and current_2 that are the heads of each inputted linked list respectovely
# while current_1 and current_2 are not null (None), loop through the lists
# check if the value current_1 is less than the value of current_2, if is is: then set tail.next to current_1 and current_1 to current_1.next
# if it is not, set tail.next to current_2 and current_2 to current_2.next
# make the tail be equal to tail.next after the if statements
# check if current_1 and current_2 are not none outside the loop, set them to tail.next if they are not
# return fake_head.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is not None and list2 is None:
            return list1
        elif list2 is not None and list1 is None:
            return list2
        fake_head = ListNode(None)
        tail = fake_head
        current_1 = list1
        current_2 = list2
        while current_1 is not None and current_2 is not None:
            if current_1.val < current_2.val:
                tail.next = current_1
                current_1 = current_1.next
            else:
                tail.next = current_2
                current_2 = current_2.next
            tail = tail.next
        if current_1 is not None:
            tail.next = current_1
        if current_2 is not None:
            tail.next = current_2
        return fake_head.next
