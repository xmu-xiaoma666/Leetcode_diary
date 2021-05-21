## 392. 判断子序列

https://leetcode-cn.com/problems/is-subsequence/



### 题目描述

```
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

 

示例 1：

输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：

输入：s = "axc", t = "ahbgdc"
输出：false
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```



### 思路

```
法一：
双指针
定义两个指针，依次从左往右遍历，t指针先结束，那么就False；否则就是True

法二：
动态规划
建立一个二维数组，记录下t每个位置的26个单词下一次出现的位置。遍历s，找到s[i]在t中下一次的出现的位置，直接跳到i+1行。如果下一次出现的位置为t的长度（也就是不出现），返回False。如果遍历完成，返回True。

```



### python代码

执行用时：
36 ms
, 在所有 Python3 提交中击败了
89.82%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
88.08%
的用户

```

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        id_s=0
        id_t=0
        while(id_s<len(s) and id_t<len(t)):
            if(s[id_s]==t[id_t]):
                id_s+=1
                id_t+=1
            else:
                id_t+=1
        if(id_s==len(s)):
            return True
        else:
            return False

```

执行用时：
168 ms
, 在所有 Python3 提交中击败了
5.25%
的用户
内存消耗：
17.7 MB
, 在所有 Python3 提交中击败了
5.04%
的用户
```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s,len_t=len(s),len(t)
        ms=[[0]*26 for _ in range(len_t)]
        ms.append([len_t]*26)

        #记录下t中每个单词下一次出现的位置
        for i in range(len_t-1,-1,-1):
            for j in range(26):
                ms[i][j]=ms[i+1][j] if j!=ord(t[i])-ord('a') else i

        for item in ms:
            print(item)
        # print(ms)

        #遍历s
        row=0
        for j in range(len_s):
            word_idx=ord(s[j])-ord('a')
            if(ms[row][word_idx]==len_t):
                return False
            else:
                row=ms[row][word_idx]+1
        return True
```
