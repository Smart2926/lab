def count_list(N):
    count=0
    for _ in N:
        count+=1
    return count
def form_number(N, K):
    M = ""
    for i in range(K - 1, count_list(N), K):
        M = M + N[i]
    return M

def is_happy_number(M):
    if int(M) % 3 == 0:
        return "YES"
    else:
        return "NO"

N = input("Введіть число N: ")
K = int(input("Введіть ключ K (від 1 до 10): "))

if K < 1 or K > 10 or K > count_list(N):
    print("Число M: ")
    print("NO")  
else:
    M = form_number(N, K)
    print("Число M:", M)
    print(is_happy_number(M))

lst_1 = [1,6,23424,8]
def count_list(N):
    count=0
    for _ in N:
        count+=1
    return count
result=count_list(N)
print(result)

set_1={4,2,2,9}
set_2={1,2}
set_3=set_1|set_2
print(set_3) 

