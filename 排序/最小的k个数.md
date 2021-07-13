## 剑指 Offer 40. 最小的k个数

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/



### 题目描述

```
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
排序，拿出前k个数
```



### python代码
执行用时：
48 ms
, 在所有 Python3 提交中击败了
97.78%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
96.17%
的用户
```
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
```

