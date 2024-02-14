# file : ds09_simpleLinkedList.py
# desc : 단순연결리스트 전체 구현

# 노드 클래스 

# 노드 클래스
class Node():
    data = None # 실제 데이터 변수
    link = None # 다음 노드를 지정하는 변수

    def __init__(self) -> None:
        self.data = None # 클래스자신이 self이므로 클래스의 변수에 접근하려면 반드시 self.
        self.link = None

def printNodes(start): # start 부터 시작해서 끝까지 노드.data 출력
    curr = start # start == head
    if curr == None: return # break , continue는 반복문없으면 안됨
    while True:
        if curr.link == None:
            print(curr.data) #자기 데이터만 출력하고 
            break # 반복문 탈출
        else:
            print(curr.data, end=' -> ') # 연결할 노드가 있으니까 연결표기 -> 를 해주고
            curr = curr.link #자기 뒤의 데이터를 curr로 바꿔줌 

# 노드 삽입함수 
def insertNode(find , data):
    global head , prev , curr

    if  head.data == find: #맨 첫번째 노드
        node = Node()
        node.data = data
        node.link = head 
        head = node
        return # 함수 탈출
    
    curr = head 
    while curr.link != None: #중간에 노드 삽입
        prev = curr
        curr = curr.link 
        if curr.data == find: #데이터를 찾았으면
            node = Node()
            node.data = data
            node.link = curr # 찾은 노드 앞에 새노드 연결 
            prev.link = node # 이전 노드 뒤에 새노드 연결 
            return # 함수 탈출 
        
    node = Node()
    node.data = data
    curr.link = node
    return

# 노드 삭제함수
def deletNode(data):
    global head, prev, curr
    
    if head.data == data: #첫번째 노드 삭제면
        curr = head 
        head = head.link
        del(curr)
        return # 함수 탈출 
    
    curr = head 
    while curr.link != None: # 첫번째 외 노드 삭제 
        prev = curr
        curr = curr.link

        if curr.data == data:
            prev.link=curr.link
            del(curr)
            return # 함수탈출 

# 노드 검색함수 
def findNode(find):
    global head , curr

    curr = head 
    if curr.data == find:
        return curr # 현재 노드를 리턴해주고 함수 탈출
    while curr.link != None:
        curr = curr.link # 다음노드로 
        if curr.data == find:
            return curr
    return Node() #위에 만족못하면 빈노드 리턴 함수 탈출

# 전역변수
head, prev, curr = None, None, None
originData = ['다현' , '정연', '쯔위', '사나', '지효']

# 메인코드 영역

if __name__ == '__main__':

    node = Node()
    node.data = originData[0] # = '다현'
    head = node # head node를 가리킴

    for name in originData[1:]: # 1번 인덱스부터 리스트 끝까지 반복
        prev = node
        node = Node()
        node.data = name
        prev.link = node

    # 연결리스트 구상완료 
    print('최초 구성된 연결리스트')
    printNodes(head) # 구성된 연결리스트가 맞는지 출력 확인
    # 다현 -> 정연 -> 쯔위 -> 사나 -> 지효
    print('노드 추가')
    insertNode('다현' , '정국')
    printNodes(head)
    #정국 -> 다현 -> 정연 -> 쯔위 -> 사나 -> 지효
    print('중간 노드 삽입')
    insertNode('사나' , '미미')
    printNodes(head)
    #정국 -> 
    insertNode('재남' , '알엠') # 재남이란 노드가 없으니 마지막 삽입 
    print('마지막 노드 삽입')
    printNodes(head)
    #정국 -> 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효 -> 알엠
    
    #노드 삭제
    deletNode('정국')
    print('맨 앞 노드 삭제')
    printNodes(head)
    # 다현 -> 정연 -> 쯔위 -> 미미 -> 사나 -> 지효 -> 알엠

    deletNode('쯔위')
    print('중간노드 삭제')
    printNodes(head)
    # 다현 -> 정연 -> 미미 -> 사나 -> 지효 -> 알엠

    deletNode('재남')
    print('없는노드 삭제')
    printNodes(head)
    # 다현 -> 정연 -> 미미 -> 사나 -> 지효 -> 알엠

    # 노드검색
    fNode = findNode('다현')
    print(f'찾은 노드 : {fNode.data}')
    
    fNode = findNode('쯔위')
    printNodes(head)
    print(f'찾은 노드 : {fNode.data}')
    



    
    






















