## 剑指 Offer 57 - II. 和为s的连续正数序列


https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/


### 题目描述

```
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
双指针
滑动窗口
```



### python代码
执行用时：
296 ms
, 在所有 Python3 提交中击败了
21.11%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
55.57%
的用户
```
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        nums=list(range(0,target//2+3))
        res=[]
        l=1
        r=2
        while(r<len(nums)):
            if(sum(nums[l:r])<target):
                r+=1
            elif(sum(nums[l:r])>target):
                l+=1
            else:
                res.append(nums[l:r])
                r+=1
        return res

```

