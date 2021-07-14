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
def pre_order(res,root):
    if(root==None):
        return
    res.append(root.val)
    if(root.left):
        pre_order(res,root.left)
    if(root.right):
        pre_order(res,root.right)

# 左，根，右
def mid_order(res,root):
    if(root==None):
        return
    if(root.left):
        mid_order(res,root.left)
    res.append(root.val)
    if(root.right):
        mid_order(res,root.right)

# 左，右，根
def back_order(res,root):
    if(root==None):
        return
    if(root.left):
        back_order(res,root.left)
    if(root.right):
        back_order(res,root.right)
    res.append(root.val)


if __name__ == '__main__':
    nums=['1', '2', '3', '#', '4', '5', '6']
    root=createTree(None,nums,0)
    res=[]
    back_order(res,root)
    print(res)
    