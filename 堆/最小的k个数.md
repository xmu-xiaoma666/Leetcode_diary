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
维护一个大根堆（小根堆的相反数）
一直pop，使得里面的数只有k个
然后把相反数取出来
```



### python代码
执行用时：
48 ms
, 在所有 Python3 提交中击败了
94.89%
的用户
内存消耗：
16.5 MB
, 在所有 Python3 提交中击败了
19.62%
的用户
```
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        hp=[-x for x in arr]
        heapq.heapify(hp)
        while(len(hp)>k):
            heapq.heappop(hp)
        res=[-x for x in hp]
        return res




```

