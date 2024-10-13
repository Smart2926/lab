def form_number(N, K):
    M = ""
    for i in range(K - 1, len(N), K):
        M = M + N[i]
    return M

def is_happy_number(M):
    if int(M) % 3 == 0:
        return "YES"
    else:
        return "NO"

N = input("Введіть число N: ")
K = int(input("Введіть ключ K (від 1 до 10): "))

if K < 1 or K > 10 or K > len(N):
    print("Число M: ")
    print("NO")  
else:
    M = form_number(N, K)
    print("Число M:", M)
    print(is_happy_number(M))