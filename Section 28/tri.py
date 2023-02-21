import random
# Section 28
# 196

# l = [5,8,10,2,1]

# l.sort()
# print(l)


# def generate_random_list(nb, min, max):
#     liste = []
#     for i in range(nb):
#         number = random.randint(min, max)
#         liste.append(number)
            
#     return liste



# def selected_sort(nb, min_list, max_list):
#     l = generate_random_list(nb, min_list, max_list)
    
#     for unsorted_index in range(0, nb-1):
#         min = l[unsorted_index]
#         min_index = unsorted_index
#         for i in range(unsorted_index+1, len(l)):
#             if l[i] < min:
#                 min = l[i]
#                 min_index = i
        
#         l[min_index] = l[unsorted_index]
#         l[unsorted_index] = min
        
#     print(l)

# selected_sort(4,0,10)

print(random.randint(0,10))