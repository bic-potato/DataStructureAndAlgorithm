import time
list1 = range(1000)
list2 = range(10000)
list3 = range(100000)

time0 = time.perf_counter()
time1 = time.perf_counter()
a = list1[499]
time2 = time.perf_counter()
a = list2[499]
time3 = time.perf_counter()
a = list3[499]
time4 = time.perf_counter()
print(f"在长度100的数组里，索引第500个数据所用时间为{time2 - time1}；在长度1000的数组里，索引第500个数据所用时间为{time3 - time2}；在长度1000的数组里，索引第500个数据所用时间为{time4 -time3}。")

dict1 = {"a":"1", "b":2, "c": "3", "IP": "127.0.0.0"}
dict2 = {"a":"1", "b":2, "c": "3", "IP": "127.0.0.0", "domain":"bicpotato.net", "overleaf": "overleaf.bicpotato.net"}
time5 = time.perf_counter()
dict1["IP"]
time6 = time.perf_counter()
dict2["IP"]
time7 = time.perf_counter()
print(f"长度为四的数组中索引时间为{time7 - time6}，长度为6的数组中索引时间为{time6 - time5}")
time8 = time.perf_counter()
dict1["drive"] = "drive.bicpotato.net"
time9 = time.perf_counter()
dict2["drive"] = "drive.bicpotato.net"
time10 = time.perf_counter()
print(f"长度为四的数组中索引时间为{time9 - time8}，长度为6的数组中索引时间为{time10 - time9}")