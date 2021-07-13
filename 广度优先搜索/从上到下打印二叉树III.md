## 剑指 Offer 32 - III. 从上到下打印二叉树 III

https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/



### 题目描述

```

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



### 思路

```
层次遍历
如果是奇数层
就翻转列表
```



### python代码
执行用时：
36 ms
, 在所有 Python3 提交中击败了
89.88%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
39.82%
的用户
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        mark=0
        queue=[]
        res=[]
        if(not root):
            return []
        else:
            queue.append(root)

        while(len(queue)>0):
            tmp=[]
            for i in range(len(queue)):
                cur=queue.pop(-1)
                if(cur.left!=None):
                    queue.insert(0,cur.left)
                if(cur.right!=None):
                    queue.insert(0,cur.right)
                tmp.append(cur.val)
            mark+=1
            if(mark%2==1):
                res.append(tmp)
            else:
                res.append(tmp[::-1])
        return res


```

