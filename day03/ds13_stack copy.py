# file : ds11_stack.py
# desc : 스택 전체 구현

import webbrowser
import time

def isStackFull():
    global SIZE, stack , top 
    if top == (SIZE - 1):
        return True
    else:
        return False
    

def push(data):
    global SIZE, stack, top
    if isStackFull() == True:
        print('스택이 꽉찼습니다.')
        return
    else:
        top += 1
        stack[top] = data
    
def isStackEmpty():
    global SIZE , stack , top
    if top <= -1:
        return True
    else:
        return False

#스택 데이터 추출함수
def pop():
    global SIZE, stack,top
    if isStackEmpty() == True:
        print('스택이 비었습니다')
        return None
    else: 
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

def peek():
    global stack, top
    if isStackEmpty() == True:
        print('스택이 비어있습니다.')
        return None
    else:
        return stack(top)
    
#전역변수 선언 
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == '__main__':
    urls  = ['naver.com','daum.net','nate.com','bing.com','github.com']

    for url in urls:
        push(url)
        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1)

    print('방문종료')
    time.sleep(5) # 5초동안 아무것도 하지 않고 대기함 

    print(stack)

    while True:
        url = pop()
        if url == None: break

        webbrowser.open(f'https://www.{url}')
        print(url , end=' --> ')
        time.sleep(1)
        
    print('방문종료')