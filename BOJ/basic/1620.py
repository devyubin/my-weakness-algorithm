# 나는야 포켓몬 마스터 이다솜

# 첫 글자만 대문자이고, 나머지 문자는 소문자로만. 일부 포켓몬은 마지막 문자만 대문자
# 숫자를 주면 포켓몬 이름으로, 포켓몬 이름 주면 숫자로 맞추기. (입력은 반드시 주어진 포켓몬에서만.)

n, m = map(int, input().split())
dic = {}
rev_dic = {}

for i in range(1, n+1):
    name = input()
    dic[i] = name
    rev_dic[name] = i

for _ in range(m):
    question = input()
    if question.isdigit():
        print(dic.get(int(question)))
    else:
        print(rev_dic.get(question))