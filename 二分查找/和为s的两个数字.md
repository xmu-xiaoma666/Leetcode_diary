## 剑指 Offer 57. 和为s的两个数字


https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/


### 题目描述

```
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
先确定一个值
然后用二分查找另一个值
```



### python代码

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums=nums
        def midsearch(t):
            left=0
            right=len(self.nums)-1
            while(left<=right):
                mid=(left+right)//2
                if(nums[mid]==t):
                    return t
                elif(nums[mid]<t):
                    left=mid+1
                else:
                    right=mid-1
            return None
        
        res=[]
        for i in nums:
            if(i<=target):
                b=midsearch(target-i)
                if(b!=None):
                    return [i,b]

```

