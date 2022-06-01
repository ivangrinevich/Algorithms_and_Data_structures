class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0
        self.msl = 0
        self.parent = None


class Tree(object):
    def __init__(self):
        self.root = None


def insert(x):
    parent = None
    v = my_tree.root
    while v is not None:
        parent = v
        if x < v.key:
            v = v.left
        elif x > v.key:
            v = v.right
        else:
            return
    w = Node(x)
    if parent is None:
        my_tree.root = w
    elif x < parent.key:
        parent.left = w
        w.parent = parent
    elif x > parent.key:
        parent.right = w
        w.parent = parent


def replace_child(parent, old, new):
    if parent is None:
        my_tree.root = new
    elif parent.left == old:
        parent.left = new
    elif parent.right == old:
        parent.right = new


def delete(x):
    parent = None
    v = my_tree.root
    while True:
        if v is None:
            return
        if x < v.key:
            parent = v
            v = v.left
        elif x > v.key:
            parent = v
            v = v.right
        else:  # x == v.key
            break
    if v.left is None:
        result = v.right
    elif v.right is None:
        result = v.left
    else:
        min_node_parent = v
        min_node = v.right
        while min_node.left is not None:
            min_node_parent = min_node
            min_node = min_node.left
        result = v
        v.key = min_node.key
        replace_child(min_node_parent, min_node, min_node.right)
    replace_child(parent, v, result)


def pre_order_traversal(v):
    if v is None:
        return
    queue = list()
    queue.append(v)
    while queue:
        node = queue.pop()
        f_output.write(str(node.key) + '\n')
        if is_leaf(node):
            leaves.append(node)
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)


def pre_order_traversal_1(v):
    if v is None:
        return
    queue = list()
    queue.append(v)
    while queue:
        node = queue.pop()
        if is_leaf(node):
            leaves.append(node)
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)


def is_leaf(v):
    if v.left is None and v.right is None:
        return True
    else:
        return False

with open('../Individual_task/inputs/tst.in', 'r', encoding='utf-8') as f_input, open('../Individual_task/outputs/tst.out', 'w', encoding='utf-8') as f_output:
    my_tree = Tree()
    leaves = []
    for i in f_input.readlines():
        insert(int(i))
    pre_order_traversal_1(my_tree.root)
    if len(leaves) % 2 == 1:
        delete(leaves[len(leaves) // 2].parent.key)
    pre_order_traversal(my_tree.root)
