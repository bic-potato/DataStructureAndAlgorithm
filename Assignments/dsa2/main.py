import sys
import time
import matplotlib.pyplot as plt
import random
import numpy as np
list1 = list(range(1000))
list2 = list(range(10000))
list3 = list(range(100000))

time0 = time.perf_counter()
time1 = time.perf_counter()
a = list1[499]
time2 = time.perf_counter()
a = list2[499]
time3 = time.perf_counter()
a = list3[499]
time4 = time.perf_counter()
print(
    f"在长度100的数组里，索引第500个数据所用时间为{time2 - time1}；在长度1000的数组里，索引第500个数据所用时间为{time3 - time2}；在长度1000的数组里，索引第500个数据所用时间为{time4 - time3}。")

dict1 = dict(zip(list(range(1000)), list(map(str, list(range(1000))))))
dict2 = dict(zip(list(range(100000)), list(map(str, list(range(100000))))))
time5 = time.perf_counter()
dict1[500]
time6 = time.perf_counter()
dict2[500]
time7 = time.perf_counter()
print(f"长度为四的数组中索引时间为{time7 - time6}，长度为6的数组中索引时间为{time6 - time5}")
time8 = time.perf_counter()
dict1[30] = "drive.bicpotato.net"
time9 = time.perf_counter()
dict2[30] = "drive.bicpotato.net"
time10 = time.perf_counter()
print(f"长度为四的数组中索引时间为{time9 - time8}，长度为6的数组中索引时间为{time10 - time9}")


def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    mid = len(lists) // 2
    # 递归
    listA = MergeSort(lists[:mid])
    listB = MergeSort(lists[mid:])
    return MergeSortedLists(listA, listB)


# 合并两个有序数集
def MergeSortedLists(listA, listB):
    newList = list()
    a = 0
    b = 0
    # Merge the two lists together until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
    # If listA contains more items,append them to newList
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    while b < len(listB):
        newList.append(listB[b])
        b += 1
    return newList


def ksmall(n, k):
    list1 = []
    while len(list1) < n:
        m = random.randint(0, n)
        if (m not in list1):
            list1.append(m)
    a = MergeSort(list1)
    return a[k - 1]


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        return self.select(num, 0, len(num) - 1, len(num) / 2)

    def partition(self, num, l, r):
        pivot = num[l]
        i = l
        j = r
        while i < j:
            while pivot < num[j] and i < j:
                j -= 1
            if i < j:
                num[i] = num[j]
                i += 1
            while pivot > num[i] and i < j:
                i += 1
            if i < j:
                num[j] = num[i]
                j -= 1
        num[i] = pivot
        return i

    def select(self, num, l, r, k):
        if l == r:
            return num[l]
        i = self.partition(num, l, r)
        j = i - l
        if j == k:
            return num[i]  # 分割完后，如果pivot刚刚好就是第K大，直接返回，否则还有两种情况：
        if (j < k):
            return self.select(num, i + 1, r, k - j - 1)
        else:
            return self.select(num, l, i - 1, k)


def ksmallOn(n, k):
    list1 = []
    while len(list1) < n:
        m = random.randint(0, n)
        if (m not in list1):
            list1.append(m)
    s = Solution()
    return s.select(list1, 0, n - 1, k)


y1 = [(time7 - time6) * 10 ** 7, (time6 - time5) * 10 ** 7]
y2 = [(time9 - time8) * 10 ** 7, (time10 - time9) * 10 ** 7]
y3 = [(time2 - time1) * 10 ** 7, (time3 - time2) * 10 ** 7, (time4 - time3) * 10 ** 7]
# x2 = x1 = ["1000", "100000"]
# x3 = [str(len(list1)), str(len(list2)), str(len(list3))]
# plt.bar(x1, height=y1, color='#3CB371', alpha=0.6, width=0.2)
# plt.xlabel("dict length")
# plt.ylabel(f"T/10$^-7$")
# plt.show()
# plt.bar(x2, height=y2, color='#3CB371', alpha=0.6, width=0.2)
# plt.xlabel("dict length")
# plt.ylabel(f"T/10$^-7$")
# plt.show()
# plt.bar(x3, height=y3, color='#3CB371', alpha=0.6, width=0.3)
# plt.xlabel("list length")
# plt.ylabel(f"T/10$^-7$")
# plt.show()
timea = time.perf_counter()
del list1[500]
timeb = time.perf_counter()
del dict1[500]
timec = time.perf_counter()
del list3[600]
timee = time.perf_counter()
del dict2[600]
timef = time.perf_counter()
y4 = [(timeb - timea)*10**7, (timee - timec)*10**7]
y5 = [(timec - timeb)*10**7, (timef - timee)*10**7]
x5=np.arange(2)+1
plt.bar(x5, height=y4, color='#3CB371', alpha=0.6, width=0.2, label="list" )
plt.bar(x5+0.3, height=y5, color="lightskyblue", alpha=0.6, width=0.2, label="dict")
plt.xlabel("list length")
plt.ylabel(f"T/10$^-7$")
plt.legend(loc="upper left")
plt.show()