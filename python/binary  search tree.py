# 이진 탐색 트리를 구현해보자 

a = ['apple', 'bear', 'cat', 'danger', 'equal', 'fuel', 'gear', 'hit', 'input', 'jsp', 'king in the north', 'long int', 'monkey', 'not', 'occur', 'pick', 'queen', 'registry', 'starship', 'tank', 'ufo', 'vector', 'worst', 'xenon', 'yellow', 'zebra']  # 정렬된 리스트

def search(a, key):
    root = int(len(a) / 2)   # 가운데 
    akey = a[root][0]   # 문자열의 크기를 비교하기 위해 첫 글자를 딴다. 
    if (len(a) == 0): # 리스트가 비어있으면 종료
        result = '실패'
        return result # 검색 실패 보고
    else:
        if key == akey:  # 검색 성공 보고  
            return a[root]  # 찾은 값 반환
        elif key < akey: # 키가 현재 노드보다 작으면
            result = search(a[:root], key) # 크기에 따라 리스트를 잘라서 
        else: # 키가 현재 노드보다 크면
            result = search(a[root + 1:], key)
    return result

key = input("소문자 알파벳을 입력하세요 ")
result = search(a, key)
print(result)
