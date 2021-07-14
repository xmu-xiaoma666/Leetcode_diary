class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def createTree(root,nums,i):
    if(i<len(nums)):
        if(nums[i]=='#'):
            return None
        else:
            root=TreeNode(nums[i])
            root.left=createTree(root.left,nums,2*i+1)
            root.right=createTree(root.right,nums,2*i+2)
            return root
    return root

# 根，左，右
# 入队列的时候，先入右节点，再入左节点
def pre_order(root):
    if(root==None):
        return []
    queue=[root]
    res=[]
    while(len(queue)>0):
        cur=queue.pop(-1)
        res.append(cur.val)
        if(cur.right):
            queue.append(cur.right)
        if(cur.left):
            queue.append(cur.left)
    return res


# 左，根，右
def mid_order(root):
    if(root==None):
        return []
    queue=[]
    res=[]
    while root or queue:
        while(root!=None):
            queue.append(root)
            root=root.left
        if(queue):
            root=queue.pop(-1)
            res.append(root.val)
            root=root.right
    return res


# 根，右，左->左，右，根
def back_order(root):
    if(root==None):
        return
    queue=[root]
    res=[]
    while(queue):
        root=queue.pop(-1)
        res.append(root.val)
        if(root.left):
            queue.append(root.left)
        if(root.right):
            queue.append(root.right)
        
    res=res[::-1]
    return res

if __name__ == '__main__':
    nums=['1', '2', '3', '#', '4', '5', '6']
    root=createTree(None,nums,0)
    res=back_order(root)
    print(res)
    