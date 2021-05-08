## [303. 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable/)





### 题目描述

```
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 

示例：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
 

提示：

0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
最多调用 104 次 sumRange 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
这道题其实就是多次计算i到j的和，如果每次每次调用 sumRange 时，都遍历 i 到 j 之间的元素，进行累加，那么每次的时间复杂度就是 $O(n**2)$

如果进行n次调用，那么时间复杂度就是 $O(n**3)$

因此，就可以用动态规划的思想，用空间换时间。先计算0到i的和，保存到一个数组sums中。那么i到j的和就是sums[j]-sums[i]，每次的时间复杂度是$O(1)$，总的时间复杂度为$O(n)$.

```



### python代码
执行用时：
68 ms
, 在所有 Python3 提交中击败了
79.93%
的用户
内存消耗：
18.2 MB
, 在所有 Python3 提交中击败了
21.96%
的用户
```
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.sums=[0]*(len(nums)+1)
        self.sums[0]=nums[0]
        for i in range(1,len(nums)):
            self.sums[i]=self.sums[i-1]+nums[i]



    def sumRange(self, left: int, right: int) -> int:
        
        return self.sums[right]-self.sums[left]+self.nums[left]

```

