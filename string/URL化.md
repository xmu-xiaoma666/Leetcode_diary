## 面试题 01.03. URL化


https://leetcode-cn.com/problems/string-to-url-lcci/


### 题目描述

```
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

 

示例 1：

输入："Mr John Smith    ", 13
输出："Mr%20John%20Smith"
示例 2：

输入："               ", 5
输出："%20%20%20%20%20"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-url-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
```



### python代码
执行用时：
52 ms
, 在所有 Python3 提交中击败了
78.85%
的用户
内存消耗：
20 MB
, 在所有 Python3 提交中击败了
76.49%
的用户
```
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        s=S[:length]
        s=s.replace(" ","%20")
        return s
```

