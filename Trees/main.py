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
    elif x > parent.key:
        parent.right = w


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


def height(v):
    prev = None
    h = 0
    s = []
    max_msl = -(1 << 30) * 2 - 1
    while True:
        while v:
            v.height = 0
            s.append(v)
            v = v.left
        if not s:
            break
        v = s[-1]
        if v.right and v.right != prev:
            s[-1].height = h
            v = v.right
            h = 0
        else:
            prev = v
            v = None
            prev.height = max(h, prev.height)
            if prev.left and prev.right:
                prev.msl = prev.left.height + prev.right.height + 2
            elif prev.left:
                prev.msl = prev.left.height + 1
            elif prev.right:
                prev.msl = prev.right.height + 1
            if prev.msl > max_msl:
                max_msl = prev.msl
            h = max(h, prev.height) + 1
            s.pop()
    return max_msl


def find_second_val(v):
    min_node_parent = v
    min_node = v.left
    if min_node is None:
        return min_node_parent
    while min_node.left is not None:
        min_node = min_node.left
    return min_node


def delete_second_val(v, max_v):
    roots = []
    queue = list()
    queue.append(v)
    while queue:
        node = queue.pop()
        if node.msl == max_v:
            roots.append(node)
        if node.right is not None:
            node.right.parent = node
            queue.append(node.right)
        if node.left is not None:
            node.left.parent = node
            queue.append(node.left)
    roots.sort(key=lambda x: x.key)
    i = roots[0]
    if i.left:
        while i.left is not None:
            if i.right and i.right.height > i.left.height:
                if i not in roots:
                    break
            parent = i
            i = i.left
        if not i.right:
            i = parent
        else:
            i = i.right
            while i.left is not None:
                if i.right and i.right.height > i.left.height:
                    if i not in roots:
                        break
                i = i.left
    else:
        i = i.right
        while i.left is not None:
            if i.right and i.right.height > i.left.height:
                if i not in roots:
                    break
            i = i.left
    delete(i.key)

def pre_order_traversal(v):
    if v is None:
        return
    queue = list()
    queue.append(v)
    while queue:
        node = queue.pop()
        f_output.write(str(node.key) + '\n')
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)


with open('../inputs/in.txt', 'r', encoding='utf-8') as f_input, open('../outputs/out.txt', 'w', encoding='utf-8') as f_output:
    my_tree = Tree()
    tree = int(f_input.readline())
    insert(tree)
    tree = f_input.readline()
    while tree != '':
        insert(int(tree))
        tree = f_input.readline()
    max_val = height(my_tree.root)
    delete_second_val(my_tree.root, max_val)
    pre_order_traversal(my_tree.root)

