nums_a = input().strip().split()
nums_b = input().strip().split()

set_nums = set(nums_a) ^ set(nums_b)
nums_list = []

for n in set_nums:
    nums_list.append(n)

nums_list.sort()

print(" ".join(nums_list))
