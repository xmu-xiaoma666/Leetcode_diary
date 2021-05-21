## 面试题 08.01. 三步问题

https://leetcode-cn.com/problems/three-steps-problem-lcci/



### 题目描述

```

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



### 思路

```
跟[爬楼梯](./Climbing_Stairs.md)一样，把每次最多两级楼梯改成了三级楼梯，注意每次结果对1000000007求余

因为每次只需要用到前三个阶梯的累计走法，也可以用动态数组
```



### python代码
执行用时：
568 ms
, 在所有 Python3 提交中击败了
25.02%
的用户
内存消耗：
50.1 MB
, 在所有 Python3 提交中击败了
41.35%
的用户
```
class Solution:
    def waysToStep(self, n: int) -> int:
        methods=[0]*(n+5)
        methods[0]=0
        methods[1]=1
        methods[2]=1+methods[1]
        methods[3]=1+methods[1]+methods[2]
        for i in range(4,n+5):
            methods[i]=(methods[i-1]+methods[i-2]+methods[i-3])%1000000007
        return methods[n]
```


执行用时：
356 ms
, 在所有 Python3 提交中击败了
70.55%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
58.49%
的用户

```
class Solution:
    def waysToStep(self, n: int) -> int:
        if(n==1):
            return 1
        elif(n==2):
            return 2
        elif(n==3):
            return 4

        a=1 #i-3
        b=2 #i-2
        c=4 #i-1
        for i in range(4,n+1):
            res=(a+b+c)%1000000007
            a,b,c=b,c,res
        return res
```