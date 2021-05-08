####  [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)



### 题目描述

```
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
本问题其实常规解法可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和
爬上 n-1 阶楼梯的方法数量，因为再爬1阶就能到第n阶。
爬上 n-2 阶楼梯的方法数量，因为再爬2阶就能到第n阶。

```



### python代码

法1：优化的递归

执行用时：28 ms, 在所有 Python3 提交中击败了98.71%的用户

内存消耗：14.7 MB, 在所有 Python3 提交中击败了83.69%的用户

```
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
```

法2：动态规划

执行用时：32 ms, 在所有 Python3 提交中击败了93.90%的用户

内存消耗：14.9 MB, 在所有 Python3 提交中击败了9.78%的用户

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(max(n+1,3))
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
```

