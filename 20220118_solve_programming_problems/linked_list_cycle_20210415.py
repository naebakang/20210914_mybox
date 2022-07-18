# File encoding: UTF-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        print(head)
        ans = True
        return ans


# ex_input
head = [3, 2, 0, -4]
pos = 1


b = ListNode(head)
aaa = Solution()
ans = aaa.has_cycle(head=b)



# ex_input
head = [3, 2, 0, -4]
pos = 1
if 0 <= pos < len(head):
    ans = True

else:
    ans = False
print(ans)

