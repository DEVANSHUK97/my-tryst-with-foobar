from collections import deque
# h = 5
# q = [19,14,28]
h = 3
q = [7,3,5,1]
p = list(range(1,2**h))
class TreeNode:
    idx = 0
    def __init__(self, value = 0):
        self.value = value
        self.left = None
        self.right = None
        
    def in_order_traversal(self):
        if self == None:
            return
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()
    
    def post_order_traversal(self):
        if self == None:
            return
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)
    
    def post_order_overwrite(self):
        if self == None:
            return 
        if self.left:
            self.left.post_order_overwrite()
        if self.right:
            self.right.post_order_overwrite()
        self.value = p[TreeNode.idx]
        TreeNode.idx = TreeNode.idx + 1

    def level_order_traversal(self):
        ans = []
        queue = deque()
        queue.append(self)
        while queue:
            focus = queue.popleft()
            ans.append(focus.value)
            if focus.left != None:
                queue.append(focus.left)
            if focus.right != None:
                queue.append(focus.right)
        return ans
                
        

def make_balanced_tree(h, idx = 0):
    if h < 1:
        return None, idx
    elif h == 1:
        root = TreeNode(p[idx])
        return root, idx + 1
    else:
        root = TreeNode(p[idx])
        idx = idx + 1
        root.left, idx = make_balanced_tree(h-1, idx)
        root.right, idx = make_balanced_tree(h-1, idx)
        return root, idx
    
root, last_idx = make_balanced_tree(h,0)
root.post_order_overwrite()
root.post_order_traversal()
root.in_order_traversal()

required_list = root.level_order_traversal()

ans = []

for x in q:
    idx = required_list.index(x)
    if idx == 0:
        ans.append(-1)
    else:
        ans.append(required_list[(idx-1)//2])

print("++++++++++++++++++++++++++++++++++++")
print(ans)