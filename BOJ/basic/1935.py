# 후위 표기식 2
# ABC*+DE/-   ---> 1*2+3/4-5

def cal(str, n1, n2):
    if str == '+':
        q.append(n1 + n2)
    elif str == '-':
        q.append(n1 - n2)
    elif str == '/':
        q.append(n1 / n2)
    elif str == '*':
        q.append(n1 * n2)


n = int(input())
words = input()
q = []
nums = [0]*n

for i in range(n):
    nums[i] = int(input())

for word in words:
    if word.isalpha():
        q.append(nums[ord(word) - ord('A')])
    else:
        num2 = q.pop()
        num1 = q.pop()
        cal(word, num1, num2)

print('%.2f' %q[0])