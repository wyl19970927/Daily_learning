class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#  建立二叉树
def create(root):
    a = input("请输入元素,‘0’表示该位置为空")
    if a == '0':
        root = None
    else:
        root = Node(a)
        root.left = create(root.left)
        root.right = create(root.right)
    return root


#  前序遍历
def presearch(root):
    if root is None :
        return None
    else:
        print(root.data)
        presearch(root.left)
        presearch(root.right)


#   中序遍历
def midsearch(root):
    if not root:
        return None
    else:
        midsearch(root.left)
        print(root.data)
        midsearch(root.right)


#  后序遍历
def postsearch(root):
    if not root:
        return None
    else:
        postsearch(root.left)
        postsearch(root.right)
        print(root.data)


root = None
r = create(root)
print("前序遍历结果：")
presearch(r)
print("中序遍历结果：")
midsearch(r)
print("后序遍历结果：")
postsearch(r)