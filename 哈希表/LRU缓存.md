## 面试题 16.25. LRU 缓存


https://leetcode-cn.com/problems/lru-cache-lcci/


### 题目描述

```

设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。

它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
通过次数24,747提交次数45,716

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



### 思路

```
每次put的时候看是否超过长度
并把当前元素放到最后一个
如果超过
pop出第一个元素
get的时候，把get的元素放到最后一个
```



### python代码
执行用时：
144 ms
, 在所有 Python3 提交中击败了
92.43%
的用户
内存消耗：
23.3 MB
, 在所有 Python3 提交中击败了
72.11%
的用户
```
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic=collections.OrderedDict()


    def get(self, key: int) -> int:
        if(key in self.dic):
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        self.dic[key]=value
        self.dic.move_to_end(key)
        if(len(self.dic)>self.capacity):
            self.dic.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

