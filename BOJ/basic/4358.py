# 생태학

from collections import defaultdict

tree_dict = defaultdict(int)
cnt = 0

while True:
    tree = input()
    if tree == "":
        break
    tree_dict[tree] += 1
    cnt += 1

sorted_trees = sorted(tree_dict.items(), key=lambda item: item[1], reverse=True)

for k, v in sorted_trees:
    print(k, round((v / cnt) * 100, 4))
