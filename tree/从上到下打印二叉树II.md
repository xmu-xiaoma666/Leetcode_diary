## 剑指 Offer 32 - II. 从上到下打印二叉树 II

https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/



### 题目描述

```
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
其实就是一个BFS，每次把左右节点都放到队列中，然后每次都把队列中的样本val取出，然后再把它们的左右节点加入到队列中
```



### python代码

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        queue=[]
        if(root==None):
            return res
        else:
            queue.append(root)
            while(queue):
                tmp=[]
                for i in range(len(queue)):
                    item=queue.pop(0)
                    if(item.left!=None):
                        queue.append(item.left)
                    if(item.right!=None):
                        queue.append(item.right)
                    tmp.append(item.val)
                res.append(tmp)
            return res

```

