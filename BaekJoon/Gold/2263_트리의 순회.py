n = int(input())

nodes = [-1]+sorted([[idx, number, -1, -1] for idx, number in enumerate(map(int,input().split()), start=1)], key=lambda x: x[1])
post = list(map(int, input().split()))[::-1]

def preorder(start):
    print(start, end=' ')
    if nodes[start][2] != -1:
        preorder(nodes[start][2])
    if nodes[start][3] != -1:
        preorder(nodes[start][3])



for node in post:
    current_node = post[0]
    if node == post[0]:
        continue
    while True:
        if nodes[node][0] < nodes[current_node][0]:
            if nodes[current_node][2] != -1:
                current_node = nodes[current_node][2]
                continue
            else:
                nodes[current_node][2] = node
                break
        elif nodes[node][0] > nodes[current_node][0]:
            if nodes[current_node][3] != -1:
                current_node = nodes[current_node][3]
                continue
            else:
                nodes[current_node][3] = node
                break
        else:
            break


preorder(post[0])





