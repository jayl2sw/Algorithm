def preorder(node):
    print(tree[node][1], end='')
    if tree[node][2]:
        preorder(tree[node][2])
    if tree[node][3]:
        preorder(tree[node][3])


def midorder(node):
    if tree[node][2]:
        midorder(tree[node][2])
    print(tree[node][1], end='')
    if tree[node][3]:
        midorder(tree[node][3])


def postorder(node):
    if tree[node][2]:
        postorder(tree[node][2])
    if tree[node][3]:
        postorder(tree[node][3])
    print(tree[node][1], end='')


n = int(input())
tree = [[i, chr(65+i), None, None] for i in range(n)]
for i in range(n):
    node, left, right = input().split()
    if left != '.':
        tree[ord(node)-65][2] = ord(left)-65
    if right != '.':
        tree[ord(node) - 65][3] = ord(right)-65


preorder(0)
print()
midorder(0)
print()
postorder(0)
