# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        head=tail=None
        #首先判断是否为空
        while (l1 or l2):
            #载入每个node的value
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            #每位相加(含上次计算得到的进位)
            everyone_place_sum=x+y+carry
            #计算进位并指向下个节点
            if head==None:
                head=tail=ListNode(everyone_place_sum%10)
            else:
                #新生成一个对象附到next上
                tail.next=ListNode(everyone_place_sum%10)
                #步进到新节点上
                tail = tail.next
            #取整算进位
            carry=everyone_place_sum//10
            #尾node需要进位的话，不加这个会被丢弃（上一位tail.next==None）（坑死我了/(ㄒoㄒ)/~~）
            if carry > 0:
                tail.next = ListNode(carry)
            #l1\l2向下步进一个node
            if l1: l1=l1.next
            if l2: l2=l2.next
        return head
