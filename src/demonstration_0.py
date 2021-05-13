"""
Purpose:
    Transverse to find existing node. 
    traversing to go thtrough any type of tree or graph
    unlike linear datastructures(array, linkedlist, queue, stacks), Hierarchical structures like trees, there are multiple ways to transverse data. (depth-first,  breadth-first)
Uses:
Advantages:
Weaknesss;

-Breadth-First      visit all nodes at level before nextlevel 0(n^2)time 0(n)space.   queue FIFO

-Depth-First        exhaust one side first(leftsub) [root, go, visit ]   recursion callstack LIFO
    --Inorder       left,   root,         right               |     [4, 2, 5, 1, 3]
    --Preorder      node     left,        right  /right, left |     [1, 2, 4, 5, 3]
    --Postorder     left,   right,        node                |     [4, 5, 2, 3, 1]
                                                                1
                                                              /   \
                                                            2       3    
                                                         /   \               
                                                        4     5         

"""
# --------------------------------------------------------------------------------
#                               DEPTH_ IN-ORDER TRAVERSAL
# ________________________________________________________________________________
"""
transverse left subtree (call preorder(left))
visit root
transverse right subtree (call preorder(right))
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)              # recur on left
        res.append(root.val)                 # visit node
        helper(root.right, res)             # recur on left

    def inorder_traversal(root):
        result = []
        helper(root, result)
        return result


# --------------------------------------------------------------------------------
#                               DEPTH_ PRE-ORDER TRAVERSAL
# ________________________________________________________________________________
"""
visit root
transverse left subtree (call preorder(left))
transverse right subtree (call preorder(right))
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def helper(root, res):
        if root is None:
            return
        res.append(root.val)                # visit node, then go to left/right
        helper(root.left, res)              # recur on left
        helper(root.right, res)

    def preorder_traversal(root):
        result = []
        helper(root, result)
        return result


# --------------------------------------------------------------------------------
#                               DEPTH_ POST-ORDER TRAVERSAL
# ________________________________________________________________________________
"""
transverse left subtree (call preorder(left))
transverse right subtree (call preorder(right))
visit root                                          basically the opposite of breadth-first
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)          # recur on left
        helper(root.right, res)
        # after recursing left & right subtrees
        res.append(root.val)            # visit root

    def postorder_traversal(root):
        result = []
        helper(root, result)
        return result


# --------------------------------------------------------------------------------
#                               BREADTH_ LEVEL ORDER TRAVERSAL
# ________________________________________________________________________________
"""
create empty queue
start from root
loop while root/node not null
    print node --> data
    enqueue leftsub, rightsub to q
    dequeue node from q
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):       # create new node
        self.val = val
        self.left = left
        self.right = right

    def breadth_transveral(root):
        if root is None:
            return []
        result = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)             # level == 1
            result.append(node.val)         # add new data
            if node.left is not None:
                queue.append(node.left)     # tree enqueue --> left
            if node.right is not None:
                queue.append(node.right)    # tree enqueue --> right
            return result
