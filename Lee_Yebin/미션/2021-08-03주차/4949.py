'''
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

<입력>
하나 또는 여러줄에 걸쳐서 문자열이 주어진다.
각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

<출력>
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''

while(True):
    charList=input() # 한 줄의 문자열 리스트를 입력받음
    stack = [] # 괄호를 넣을 스택 (빈 리스트) 생성
    if charList[0]=='.': # 첫번째 문자가 '.'인 경우는 종료
        break
    for ch in charList:
        if ch=='(' or ch=='[': # 여는 괄호는 스택에 추가
            stack.append(ch)
            continue
        elif ch==')' or ch==']': # 닫는 괄호인 경우
            if not stack: # 스택이 빈 리스트인 경우(닫는 괄호가 먼저 나오는 경우) 종료
                print("no")
                break
            get=stack.pop() # 스택으로부터 괄호를 pop한 후에 닫는 괄호와 짝이 맞는지 검사
            if ch==')' and get=='(':
                continue
            elif ch==']' and get=='[':
                continue
            else:
                print("no") # 짝이 맞지 않는 경우 no 출력 후 종료
                break
        elif ch=='.': # 마지막까지 도달한 경우 yes
            if not stack:
                print("yes")
            else:
                print("no")