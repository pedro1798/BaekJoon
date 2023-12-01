import sys
input = sys.stdin.readline

# 딕셔너리의 이름 뜻을 잘 생각해보기
# 민식어를 영어에 bound 해서 정렬

minsic = {"a": "A", "b": "B", "k":"C", "d": "D", "e":"E", "g":"F", 
            "h":"G", "i":"H", "l":"I", "m":"J", "n":"K", "o":"M", "p":"N", "r":"O",
            "s":"P", "t":"Q", "u":"R", "w":"S","y":"T"}
# 민식어와 영어를 bound한다 

def minsic_to_eng(string: str):
    result = string.replace("ng", "L")
    # 영어의 어순으로 바꿀 문자열 result
    for k, v in minsic.items():
        result = result.replace(k, v)
        # result에서 민식어 k를 영어 v로 바꾼다.
    return result  # 영어로 번역한 민식어를 반환한다.
        
    
def sol(minsics):
    result = dict()
    for m in minsics: 
        translated_to_eng = minsic_to_eng(m)
        result[m] = translated_to_eng  # 민식어 : 영어 의 key value 쌍 딕서너리를 만든다
    result = sorted(result.items(), key = lambda x : x[1])  # 영어의 사전순으로 정렬한다.
    # result.items()는 tuple을 반환한다.
    # x[1] value로 정렬
    return result


if __name__ == "__main__":
    minsics = list()
    for _ in range(int(input())) :
        minsics.append(input().rstrip())
    result = sol(minsics)
    for i in result :
        print(i[0])
