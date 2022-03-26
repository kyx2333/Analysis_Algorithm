# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 上一个节点，当前节点
        last, left = head,head
        flag = True
        count = 0
        while left != None:
            # 指向下一个节点
            right = left.next
            # 判断当前指向的节点值是否等于指向下一个节点相等
            if right != None and right.val == left.val:
                while right != None and right.val == left.val:
                    # 移动下一个指向的节点
                    right = right.next
                    if right == None:
                        left = None
                    if right != None and right.val != left.val:
                        left = right
                        right = left.next
            #如果上一个节点是第一个节点
                if last == head and count != 1:
                    head = left
                else:
                    last.next = left
            # 记录要拼接的上一个节点
            last = left
            count += 1
            # 移动当前链表节点
            if left != None:
                left = left.next

        return head
s = Solution()
put = [0,1,1,2,2,3,3,4,4,5,5,6,7,7,9]
node = ListNode(put[0])

j = node
for i in range(1,len(put)):
    j.next = ListNode(put[i])
    j = j.next
node = s.deleteDuplicates(node)
while node != None:
    print(node.val)
    node = node.next
