def isQueueFull():
    if (rear == SIZE) - 1:
        return True
    else:
        return False

def isQueueEmpty():
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global rear
    if (isQueueFull()):
        print('큐가 꽉 찼습니다.')
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global front, rear
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    for i in range(front + 1, rear + 1):
        queue[i - 1] = queue[i]
        queue[i] = None
    front = -1
    rear -= 1
    return data

def peek():
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    return queue[front + 1]

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == '__main__':
    while True:
        print("1. 웨이팅 추가\n2. 입장\n3. 웨이팅 상태 확인\n4. 종료")
        select = input("선택: ")

        if select == '1':
            name = input("웨이팅에 추가할 이름: ")
            enQueue(name)
            print(f'{name} 님이 웨이팅에 추가되었습니다.')

        elif select == '2':
            if isQueueEmpty():
                print('웨이팅이 비어있습니다.')
            else:
                print(deQueue(), '님 식당에 입장하셨습니다.')

        elif select == '3':
            print('대기열 상태:', queue)

        elif select == '4':
            print('식당 영업 종료!')
            break

        else:
            print('잘못된 선택입니다. 다시 선택해주세요.')