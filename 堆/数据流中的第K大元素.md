## 703. 数据流中的第K大元素


https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/


### 题目描述

```
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
 

示例：

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

提示：
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
最多调用 add 方法 104 次
题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
通过次数56,736提交次数110,975

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
第K大的元素
维护一个小根堆
然后保持这个堆的长度为k
最后这个堆中就是前K大的元素了
最后拿出que[0]就可以啦
```



### python代码
执行用时：
72 ms
, 在所有 Python3 提交中击败了
94.68%
的用户
内存消耗：
18.5 MB
, 在所有 Python3 提交中击败了
34.88%
的用户
```
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.que=nums
        heapq.heapify(self.que)
        



    def add(self, val: int) -> int:
        heapq.heappush(self.que,val)
        while(len(self.que)>self.k):
            heapq.heappop(self.que)
        return self.que[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

