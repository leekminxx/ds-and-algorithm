# file : ds19_binarySearchTree.py
# desc : 이진검색트리 구현 

class TreeNode():
    left = data = right = None

    def __init__(self) -> None:
        self.left = self.right = self.data = None

# 중위 순회
def inorder(node):
    if node == None: return

    inorder(node.left)
    print(node.data, end=' -> ')
    inorder(node.right)

# 전역변수
root = None
groupList = ['블랙핑크' , '레드벨벳' , '마마무', '에이핑크', '걸스데이', '트와이스']

# 메인
node = TreeNode
node.data = groupList[0]
root = node

for name in groupList[1:]:
    node = TreeNode
    node.data = name
    
    curr = root
    while True:
        if name < curr.data: # 왼쪽 트리로
            if curr.left == None: #왼쪽에 트리가 구성되어있지 않으면
                curr.left == node 
                break # while문을 탈출 
            else:
                curr = curr.left 
        else:
            if curr.right == None:
                curr.right == node
                break
            else:
                curr = curr.right

print('이진 탐색트리 구성 완료!')

findname = '에이핑크'

curr = root
level = 0
while True:
    if findname == curr.data:
        print(f'{curr.data}를찾음')
        break
    elif findname < curr.data:
        if curr.left == None:
            print(f'{findname}이 트리에 없음')
            break
        else:
            curr = curr.left
            level += 1
    else: #오른쪽 트티로 
        if curr.right == None:
            print(f'{findname}이 트리에 없음')
            break
        else:
            curr = curr.right
            level += 1

curr = root
print('중위 순회 : ' ,end= '')
inorder(curr)
print('끝')

deleteName = '에이핑크'
curr = root
parent = None

while True:
    if deleteName == curr.data:
        if curr.left == None and curr.right == None:
            if parent.left == curr: # 내가 부모의 왼쪽에 붙어있으면 
                parent.left == None 
            else: # 내가 부모의 오른쪽에 붙어있으면 
               parent.right = None

           
            del(curr) #여결이 끊어진 노드를 완전 삭제
        elif curr.left != None and curr.right == None:
            if parent.left == curr: # 부모노드 왼쪽에 내가 있으면 
               parent.left = curr.left 
            else: #부모노드의 오른쪽에 내가 있으면
               parent.right = curr.left

            del(curr)
        elif curr.left == None and curr.right != None: # 내노드 오른쪽에 자식노드가 있으면 
            if parent.left == curr:
                parent.left = curr.right
            else:
                parent.right = curr.right

            del(curr)

        print(f'{deleteName}이 삭제됨')
        break


    elif deleteName < curr.data: #왼쪽으로 
        if curr.left ==None:
            print(f'{deleteName}이 트리에 없음')
            break
        else:
            parent = curr
            curr = curr.left
    else: #오른쪽으로 
        if curr.right == None:
            print(f'{deleteName} 이 트리에 없음')
            break
        else:
            parent = curr
            curr = curr.right

curr = root
print('중위 순회: ', end='')
inorder(curr)
print('끝')
