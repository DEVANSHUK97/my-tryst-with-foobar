from collections import deque

# h = 5
# q = [19,14,28]
# h = 3
# q = [7,3,5,1]
# p = list(range(1,2**h))

class TreeNode:
    idx = 0
    def __init__(self, value = 0):
        self.value = value
        self.left = None
        self.right = None

    def post_order_overwrite(self, p):
        if self == None:
            return 
        if self.left:
            self.left.post_order_overwrite(p)
        if self.right:
            self.right.post_order_overwrite(p)
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
                
        

def make_balanced_tree(h):
    if h < 1:
        return None
    elif h == 1:
        root = TreeNode(0)
        return root
    else:
        root = TreeNode(0)
        root.left = make_balanced_tree(h-1)
        root.right = make_balanced_tree(h-1)
        return root
    


def solution(h,q):
    p = list(range(1,2**h))
    root = make_balanced_tree(h)
    root.post_order_overwrite(p)
    required_list = root.level_order_traversal()
    ans = []
    for x in q:
        idx = required_list.index(x)
        if idx == 0:
            ans.append(-1)
        else:
            ans.append(required_list[(idx-1)//2])
    TreeNode.idx = 0
    return ans
