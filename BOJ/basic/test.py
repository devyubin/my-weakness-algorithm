# set을 통해 훨씬 빠르게 하나의 요소 찾기 (하지만 set은 중복 값 안들어가니 주의! + 순서 없음)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_data_set = set(data)

for i in range(100):
    if i in data:
        print(1)

# 딕셔너리를 쉽게 묶는 zip
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}

print(*_dict.keys()) # apple grape orange banana
print(*_dict.values()) # 3200 15200 9800 5000
print(*_dict.items()) # ('apple', 3200) ('grape', 15200) ('orange', 9800) ('banana', 5000)

_list = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_list)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_list, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']

string = 'I am Hungry...'
print(string[::-1])
print("".join(reversed(string)))


# combination은 모든 조합을 출력합니다. 즉, 중복이 없고, 순서를 구분하지 않습니다. permutation은 순열입니다. 중복은 없지만, 순서를 구분합니다.
import itertools
_list = [1, 2, 3, 4]
iter = itertools.combinations(_list, 2) # 12 13 14 23 24 34
iter = itertools.permutations(_list, 2) # 12 13 14 21 23 24 31 32 34 41 42 43
iter = itertools.combinations_with_replacement(_list, 2) # 11 12 13 14 22 23 24 33 34 44
iter = itertools.product(_list, repeat=2) # 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44

lst = [1, 10, 2, 6, 5, 3]
# 전체 리스트에서 3개의 요소를 추출하는 모든 조합을 생성
for combination in itertools.combinations(lst, 3):
    # 각 조합의 곱을 계산
    product = combination[0] * combination[1] * combination[2]
    # 현재까지의 최대 곱과 비교하여 갱신
    if product > max_product:
        max_product = product


# , 출력이 필요한 경우. ex. 1, 2, 3, 4
_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(', '.join(_list))

