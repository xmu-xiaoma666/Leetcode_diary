## 剑指 Offer 54. 二叉搜索树的第k大节点

https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/



### 题目描述

```
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```

左中右遍历就得到了从小到大的排序
那么右中左就得到了从大到小的排序
所以只需要遍历后拿出第k个数字就可以了

```



### python代码
执行用时：
76 ms
, 在所有 Python3 提交中击败了
13.49%
的用户
内存消耗：
18.8 MB
, 在所有 Python3 提交中击败了
21.72%
的用户
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if(root==None):
                return
            dfs(root.right)
            if(self.k==0):
                return
            #当前就是第k大的数字
            if(self.k==1):
                self.res=root.val
            self.k-=1
            dfs(root.left)
            
        self.k=k
        dfs(root)
        return self.res

```

