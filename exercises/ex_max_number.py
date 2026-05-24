num_list = [2345, 52, 86, 2453, 646, 6427, 23, 864, 239]

# stack = []
# for i in num_list:
#     if not stack:
#         stack.append(i)
#     if i > stack[0]:
#         stack.pop()
#         stack.append(i)
    
# print(stack[0])

max_num = num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num

print(max_num)