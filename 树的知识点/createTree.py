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


if __name__ == '__main__':
    nums=['1', '2', '3', '#', '4', '5', '6']
    root=createTree(None,nums,0)
    print(root)
    
