class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def preorder(n):
    print(n.root,end='')
    if n.left:
        preorder(n.left)
    if n.right:
        preorder(n.right)

def inorder(n):
    if n.left:
        inorder(n.left)
    print(n.root,end='')
    if n.right:
        inorder(n.right)

def postorder(n):
    if n.left:
        postorder(n.left)
    if n.right:
        postorder(n.right)
    print(n.root,end='')

str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
node = [0]*(n+1)

for i in range(n):
    node[i] = Node(str[i])

for i in range(n):
    root, left, right = input().split()
    if left != '.':
        node[str.find(root)].left = node[str.find(left)]
    if right != '.':
        node[str.find(root)].right = node[str.find(right)]

preorder(node[0])
print()
inorder(node[0])
print()
postorder(node[0])
print()


# n0 = Node('A')
# n1 = Node('B')
# n2 = Node('C')
# n3 = Node('D')
# n4 = Node('E')
# n5 = Node('F')
# n6 = Node('G')

# n0.left = n1
# n0.right = n2
# n1.left = n3
# n2.left = n4
# n2.right = n5
# n5.right = n6

# preorder(n0)
# print()
# inorder(n0)
# print()
# postorder(n0)
# print()