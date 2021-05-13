

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


​
   def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
​
   else:
           # the value must go right
        if self.right is None:
            self.right = BSTNode(value)
        else:
            # let the right hand Node figure it out
            self.right.insert(value)
​
   ​

       def print_tree_preorder(root):
            print(root.value)  # if you  can go left, rescurse left
            if root.left:  # is not None
                print_tree_preorder(root.left)
            if root.right:
                print_tree_preorder(root.right)

        def print_tree_inorder(root):
            if root.left:
                print_tree_inorder(root.left)

            print(root.value)
            if root.right:
                print_tree_inorder(root.right)

        def print_tree_preorder(root):
            if root.left:
                print_tree_preorder(root.left)
            if root.right:
                print_tree_preorder(root.right)
            print(root.value)

        def print_tree_preorder(root):
            if root.left:
                print_tree_preorder(root.left)
            if root.right:
                print_tree_preorder(root.right)
            print(root.value)

        ​


def breadth_first_traversal(root):
    queue = []    # create a queue
    queue.append(root)     # add the first item to the queue

​
   while len(queue) > 0:    # Process items in the queue
        node = queue.pop(0)        # dequeue an item
        print(node.value)        # evaluate the node
​
   if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
​


def depth_first_traversal(root):
    stack = []    # create a queue
    stack.append(root)    # add the first item to the queue

​
   while len(stack) > 0:    # Process items in the queue
        node = stack.pop()        # dequeue an item
        print(node.value)        # evaluate the node
​
   if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
​
​
​


def in_order_array(root):
    my_array = []

    def generate_in_order_array(root):
        if root.right:
            generate_in_order_array(root.right)
                               # print(root.value)
        my_array.append(root.value)

​
   if root.left:
        generate_in_order_array(root.left)
​
    generate_in_order_array(root)
    return my_array
​
root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)
​
# print('---- Pre order ---- ')
# print_tree_pre_order(root)
​
# print('---- in order ---- ')
# print_tree_in_order(root)
​
# print('---- post order ---- ')
# print_tree_post_order(root)
# ​
# print("BFS")
# breadth_first_traversal(root)
