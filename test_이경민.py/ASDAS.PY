
def StackFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False
    
def StackEmpty():
    global SIZE, queue, front, rear
    if rear == -1:  
        return True
    else:
        return False
    
def put_in(data):
    global SIZE, queue, front, rear
    if StackFull():
        print("Queue is Full")
        return
    rear += 1  
    queue[rear] = data

def Extraction():
    global SIZE, queue, front, rear
    if StackEmpty():
        print("Queue is Empty")
        return None
    data = queue[front+1]
    for i in range(front+1, rear):
        queue[i] = queue[i+1]  
    queue[rear] = None  
    rear -= 1  
    return data

def check():
    global SIZE, queue, front, rear
    if StackEmpty():
        print("Queue is Empty")
        return None
    return queue[front+1]


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


if __name__ == "__main__":
    while True:
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>")

        if select == 'X' or select == 'x':
            print("End of 식당")
            break

        if select == 'I' or select == 'i':
            data = input("입력 데이터 ==> ")
            put_in(data)
            print("웨이팅 상태 => ", queue)
        elif select == 'E' or select == 'e':
            data = Extraction()
            if data is not None:
                print(data, '님 입장부탁드립니다')
            print("웨이팅 상태", queue)
        elif select == 'V' or select == 'v':
            data = check()
            if data is not None:
                print("확인된 데이터 ==> ", data)
            print("웨이팅 상태", queue)
        else:
            print("입력값 잘못됨")

