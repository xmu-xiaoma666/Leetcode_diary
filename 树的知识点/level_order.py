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

def level_order(root):
    res=[]
    queue=[]
    queue.insert(0,root)
    while(len(queue)>0):
        cur=queue.pop(-1)
        print(len(queue))
        if(cur.left!=None):
            queue.insert(0,cur.left)
        if(cur.right!=None):
            queue.insert(0,cur.right)
        res.append(cur.val)
    return res


if __name__ == '__main__':
    nums=['1', '2', '3', '#', '4', '5', '6']
    root=createTree(None,nums,0)
    res=level_order(root)
    print(res)
    