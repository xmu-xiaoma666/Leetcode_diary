## 746. 使用最小花费爬楼梯


https://leetcode-cn.com/problems/min-cost-climbing-stairs/


### 题目描述

```
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

 

示例 1：

输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
 示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
动态规划的思想
n个阶梯的cost=min(n-1阶梯累计cost+cost(n-1),n-2阶梯累计cost+cost(n-2))
前两个阶梯累计的cost为0
```



### python代码
执行用时：
48 ms
, 在所有 Python3 提交中击败了
84.11%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
49.57%
的用户

```
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost=len(cost)
        if(len_cost<2):
            return 0
        acccost=[None]* (len_cost+1)
        acccost[0]=0
        acccost[1]=0
        for i in range(2,len_cost+1):
            acccost[i]=min(acccost[i-1]+cost[i-1],acccost[i-2]+cost[i-2])
        print(acccost)
        return acccost[len_cost]

```

