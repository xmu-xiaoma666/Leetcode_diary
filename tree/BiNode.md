## 面试题 17.12. BiNode





### 题目描述

```
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动

 

示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：

节点数量不会超过 100000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binode-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
中序遍历所有的节点（左中右）
```



### python代码
执行用时：
120 ms
, 在所有 Python3 提交中击败了
47.59%
的用户
内存消耗：
21.4 MB
, 在所有 Python3 提交中击败了
9.02%
的用户
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        
        self.ans=None
        self.pre=None
        
        def dfs(root):
            if(root==None):
                return

            dfs(root.left)

            if(self.ans==None):
                self.ans=root
                self.pre=root
            else:
                root.left=None
                self.pre.right=root
                self.pre=root
            
            dfs(root.right)

        dfs(root)
        return self.ans
```

