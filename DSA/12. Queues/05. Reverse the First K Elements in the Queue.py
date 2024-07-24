#
# from sys import stdin
# import queue
#
# def reverseKElements(inputQueue, k) :
#     if inputQueue.empty() or k > inputQueue.qsize() or k <= 0:
#         return inputQueue
#
#     stack = list()
#
#     for i in range(k):
#         stack.append(inputQueue.get())
#
#     while not isEmpty(stack):
#         inputQueue.put((stack.pop()))
#
#     for i in range(inputQueue.qsize() - k):
#         inputQueue.put(inputQueue.get())
#
#     return inputQueue


# n = int(input())

# from sys import stdin
#
# t = list(map(int, stdin.readline().split()))
# # t = list(map(int, input().split()))
#
# n = t[0]
# pattern_1 = n
#
# for i in range(1, n + 1):
#     pattern_3 = n
#     for k in range(1, i):
#         print(f"\033[1;31m{pattern_3}", end=" ")
#         pattern_3 -= 1
#     for j in range(1, 2 * n + 2 - 2 * i):
#         print(f"\033[1;34m{pattern_1}", end=" ")
#     pattern_1 -= 1
#     for l in range(1, i):
#         pattern_3 += 1
#         print(f"\033[1;33m{pattern_3}", end=" ")
#     print("")
#
# pattern_1 = 2
#
# for i in range(n, 1, -1):
#     pattern_3 = n
#     for k in range(1, i):
#         print(f"\033[1;32m{pattern_3}", end=" ")
#         pattern_3 -= 1
#     for j in range(1, 2 * n + 2 - 2 * i):
#         print(f"\033[1;35m{pattern_1}", end=" ")
#     pattern_1 += 1
#
#     for _ in range(1, i):
#         pattern_3 += 1
#         print(f"\033[1;38m{pattern_3}", end=" ")
#     print("")
#
# pattern_1 = n
#
# for i in range(1, n + 1):
#     pattern_3 = n
#     for k in range(1, i):
#         print(f"\033[1;31m{pattern_3}", end="")
#         pattern_3 -= 1
#
#     for j in range(1, 2 * n + 2 - 2 * i):
#         print(f"\033[1;34m{pattern_1}", end="")
#     pattern_1 -= 1
#
#     for l in range(1, i):
#         pattern_3 += 1
#         print(f"\033[1;33m{pattern_3}", end="")
#     print("")
#
# pattern_1 = 2
#
# for i in range(n, 1, -1):
#     pattern_3 = n
#     for k in range(1, i):
#         print(f"\033[1;32m{pattern_3}", end="")
#         pattern_3 -= 1
#     for j in range(1, 2 * n + 2 - 2 * i):
#         print(f"\033[1;35m{pattern_1}", end="")
#     pattern_1 += 1
#
#     for _ in range(1, i):
#         pattern_3 += 1
#         print(f"\033[1;38m{pattern_3}", end="")
#     print("")


# def binary_search_recursive(arr, low, high, target):
#     if low <= high:
#         mid = (low + high) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return binary_search_recursive(arr, mid + 1, high, target)
#         else:
#             return binary_search_recursive(arr, low, mid - 1, target)
#     else:
#         return -1
#
#
# def selection_short(arr):
#
#     for i in range(len(arr)):
#         start = i
#
#         for j in range(start, len(arr)):
#             if arr[j] <= arr[start]:
#                 start = j
#
#         arr[i], arr[start] = arr[start], arr[i]
#
# arr = list(map(int, input().split()))
# # target = int(input())
# # result = binary_search_recursive(arr, 0, len(arr) - 1, target)
#
# selection_short(arr)
# print(arr)








# def generate_primes(n):
#     primes = []
#     num = 2
#
#     while len(primes) < n:
#         is_prime = all(num % p != 0 for p in primes)
#         if is_prime:
#             primes.append(num)
#         num += 1
#
#     return primes
#
# n = int(input())
# result = generate_primes(n)
# print(result)


# n = int(input())
#
# result = lambda n : all(n % i != 0 for i in range(2, n - 1))
#
# print(result(n))


# n = int(input())

# n2 = n
# num = ""
#
# while n2 > 0:
#     num = str(num) + str(n2 % 10)
#     n2 //= 10
#
# print(n, num)


# s = str(n)
# num = s[::-1]
#
# print(n, num)
#
# if str(n) == str(num):
#     print("true")
# else:
#     print("false")




# n = 9
#
# half1 = n // 2 + 1
# half2 = n - half1
#
# for i in range(1, half1 + 1):
#     for j in range(half1 - i):
#         print(" ", end="")
#
#     for k in range(i * 2 - 1):
#         print("*", end="")
#
#     print()
#
# for i in range(1, half2 + 1):
#     for j in range(i):
#         print(" ", end="")
#
#     for k in range(1, 2 * half2 + 2 - 2 * i):
#         print("*", end="")
#
#     print()

# i=1
# while i<3:
#     j=0
#     while j<5:
#         j = j +1
#         if j==3:
#             continue
#         print(j, end = "")
#     i = i +1



# n = int(input())
#
# a = 0
# b = 1
# c = 1
#
# ans = 0
#
# while c < n:
#     if c % 2 == 0:
#         ans += c
#
#
#     c = a + b
#
#     a, b = b, c
#
#
#     print(c, ans)
# print(ans)




# def swapAlternate(arr, n) :
#     for i in range(0, n, 2):
#         if i > n - 1 or i + 1 > n:
#             break
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#
# arr = list(map(int, input().split()))
# swapAlternate(arr, len(arr))
#
# print(arr)

# arr = input().split()
#
# print(arr)
# print(arr[0])
# print(arr[1])


# mat = [[1, 2, 3, 11], [4, 5, 6, 22], [7, 8, 9, 33]]
# nRows = 3
# mCols = 3
#
# for i in mat:
#     print(*i)
#
# print()
#
# for j in range(mCols):
#     for i in range(nRows):
#         if j % 2 != 0:
#             print(mat[nRows - i - 1][j], end=" ")
#         else:
#             print(mat[i][j], end=" ")


# i = 0
# curr = ""
#
# while i < len(string):
#     if curr != string[i]:
#         curr = string[i]
#         nStr += curr
#
#     i += 1
#
# return nStr




n = 10
arr = [0] * n

val = 1
start = 0
end = n - 1

while start <= end:

    if val % 2 == 0:
        arr[end] = val
        end -= 1

    else:
        arr[start] = val
        start += 1

    val += 1


print(arr)




