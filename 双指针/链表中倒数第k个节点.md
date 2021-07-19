## 剑指 Offer 22. 链表中倒数第k个节点

https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/



### 题目描述

```

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



### 思路

```
快慢指针
先让快指针走k步
然后一起走
快指针到结尾时
慢指针就在倒数第k个位置
```



### python代码
执行用时：
36 ms
, 在所有 Python3 提交中击败了
84.74%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
22.10%
的用户
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #快慢指针
        h1=head
        h2=head
        for i in range(k):
            h2=h2.next
        while(h2):
            h1=h1.next
            h2=h2.next
        return h1
```

