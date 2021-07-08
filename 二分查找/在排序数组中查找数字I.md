## 剑指 Offer 53 - I. 在排序数组中查找数字 I

https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/



### 题目描述

```

统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



### 思路

```
二分查找当前的数
然后前面查找重复的个数
```



### python代码
执行用时：
40 ms
, 在所有 Python3 提交中击败了
74.42%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
28.34%
的用户
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        res=0
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                res=1
                m=mid
                n=mid
                while(m+1<len(nums)):
                    if(nums[m+1]==nums[m]):
                        m+=1
                        res+=1
                    else:
                        break
                        print(m)
                while(n-1>=0):
                    if(nums[n-1]==nums[n]):
                        n-=1
                        res+=1
                    else:
                        break
                        print(n)
                return res
            elif(nums[mid]<target):
                left=mid+1
            else:
                right=mid-1
        return 0

```

