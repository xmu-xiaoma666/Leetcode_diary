## 面试题 17.16. 按摩师

https://leetcode-cn.com/problems/the-masseuse-lcci/



### 题目描述

```
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动

 

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
定义 \textit{dp}[i][0]dp[i][0] 表示考虑前 ii 个预约，第 ii 个预约不接的最长预约时间，\textit{dp}[i][1]dp[i][1] 表示考虑前 ii 个预约，第 ii 个预约接的最长预约时间。

从前往后计算 \textit{dp}dp 值，假设我们已经计算出前 i-1i−1 个 \textit{dp}dp 值，考虑计算 \textit{dp}[i][0/1]dp[i][0/1] 的答案。



```



### python代码
执行用时：
36 ms
, 在所有 Python3 提交中击败了
83.52%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
9.25%
的用户

```
class Solution:
    def massage(self, nums: List[int]) -> int:
        len_nums=len(nums)
        if(len_nums==0):
            return 0
        dp= [[-1] *2] * len_nums #dp[i][0]表示第i个预约不接的最长时间，dp[i][1]表示第i个预约接受的最长时间
        dp[0][0]=0
        dp[0][1]=nums[0]
        
        for i in range(1,len_nums):
            a=max(dp[i-1][0],dp[i-1][1])
            b=dp[i-1][0]+nums[i]
            dp[i][0]=a
            dp[i][1]=b


        return max(dp[len_nums-1][0],dp[len_nums-1][1])
```

