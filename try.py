


# nums = [2,7,11,15]
#
# def length(s):
#     n = len(s)
#     ans = 0
#     mp = {}  #收集所有可能的字符串（没有重复）
#     i = 0
#     for j in range(n):  #遍历字符串
#         if s[j] in mp.keys():
#             i = max(mp[s[j]],i)
#         ans = max(ans,j-i+1)
#         mp[s[j]] = j+1
#     return ans
#
# print(length(s='bdebba'))
#
#
#
#
#
# a = {}
# b = a.keys()
#
# for i in b:
#     print(type(i))










# import os
# path = r"C:\\"
# for a,b,c in os.walk(path):
#     print(a,b,c)
#
#
# import re
#
# a = '<h2 class="blog-motto">探索一个软件工程师的无限可能</h2>'
# matched = re.search(r"blog-motto\">(.*)</h2>", a)
#
# print(matched.group(1))
# from jsonschema import  validate
# import json
# A ={
# "$schema": "http://json-schema.org/draft-07/schema#",
#
# "title": "这是title",
#
# "description": "这是描述信息 ",
#
# "type": "object",
#
# "properties": {
#
#     "name": {
#     "description": "这是name的描述信息",
#     "type": "string"
#
# }
#
# },
#
# "required": [
#
# "name"]
#
# }
#
#
#
# json_obj = { 'str': 'this is a string', 'arr': [1, 2, 'a', 'b'], 'sub_obj': { 'sub_str': 'this is sub str', 'sub_list': [1, 2, 3] }, 'end': 'end' }
#
# b = json.loads(json.dumps(json_obj))
# print(type(b))
# print(type(json.dumps(json_obj)))

# print(json.dumps((A)))
# print(type(json.dumps(A)))
# print(json.loads(A))
# print(type(json.loads(A)))







# li = [1,3,10,9,34,12,6]
#
# # for j in range(len(li)):
# #     for i in range(len(li)-1):
# #         if li[i]> li[i+1]:
# #             li[i],li[i+1] = li[i+1],li[i]
# #             print(i)
# #             print(li)
# li.sort()
# li.reverse()
# print(li)

# a = 6
# b = 7
# c = 8
# t = 50
#
# s = []
#
# for i in range(t+1):
#     s1 = a*i
#     s.append(s1)
#     for j in range(t+1):
#         s2 =  s1 +b * j
#         s.append(s2)
#         for k in range(t+1):
#             s3 = s2 + c * k
#             s.append(s3)
#
#
#
# s.sort()
# # print(s)
# news = []
#
# for i in s:
#     if i not in news:
#         news.append(i)
# print(news)
#
# r = []
# for i in range(6*t):
#     if i in news:
#         pass
#     else:
#         r.append(i)
# print(r)


# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# import requests
#
# r = requests.post()
# r.request.headers
#
#
# a = [1,54,2,3,2
#      ]
# a.sort(key=)
# print(a)
# print(a.index)
# b = list(set(a))
# print(b)
# print(b.sort(key=a.index))

# a = []
# for i in range(1,1000):
#     s = 0
#     for j in range(1,i):
#         if i % j ==0 and j < i :
#             s +=j
#     if s ==i :
#         print(i)
#         a.append(i)
# print('1000内完全数： %s' %a)
#
#
# sxh = []
#
# for i in range(100,1000):
#     s = 0
#     li = list(str(i))
#     for j in li:
#         s += int(j)** 3
#     if s == i:
#         print(s)


#
# def fib(x):
#     a,b = 0,1
#     # if x > 1:
#     #     print(b)
#
#     for j in range(x):
#         yield b
#         a,b = b,a+b
#
#
# for x in fib(10):
#     print(x)
#
# g = fib(6)
#
# while True:
#     try:
#         x = next(g)
#         print("g:" ,x )
#     except StopIteration as e:
#         print("error: " ,e.value)
#         break

# def triangles():
#     L = [1]
#     while 1:
#         yield L
#         L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
#
# g = triangles()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for x in zip([1,2],[3,4]):
#     print(x)




