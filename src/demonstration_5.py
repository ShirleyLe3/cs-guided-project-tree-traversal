# -----------------------------------------------------------------------------------------------
#                       PATH FINDING
# _______________________________________________________________________________________________


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


def print_paths(root, path):
    new_path = path + [root.value]
    print(new_path)
    if root.left:
        # if you can go left, recurse left
        print_paths(root.left, new_path.copy())
    if root.right:
        print_paths(root.right, new_path.copy())


​


def find_paths(root, path):

    print(new_path)
    if not root.left and not root.right:
        paths_array.append(new_path)
    if root.left:
        # if you can go left, recurse left
        print_paths(root.left, new_path.copy())
    if root.right:
        print_paths(root.right, new_path.copy())
    print_paths(root, [])
    return paths_array


def depth_first_traversal(root):
    paths_array = []
    stack = []                  # create a queue
    stack.append(root, [])      # add first item to queue

    while len(stack) > 0:       # process ote,s om queue
        node = stack.pop()      # dequeue item
        new_path = path + [root.value]
        print(new_path)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return paths_array


​
root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)

print_tree_pre_order(root)
