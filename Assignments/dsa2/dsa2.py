import timeit
list_get = timeit.Timer('x=l[5000]', 'from __main__ import l')
dict_get = timeit.Timer('a=dic[5000]', 'from __main__ import dic')
dict_set = timeit.Timer('dic[5000]=0', 'from __main__ import dic')
list_del = timeit.Timer('del l[5000]', 'from __main__ import l')
# dict_del = timeit.Timer(, )
for i in range(10000, 100001, 10000):
    l = list(range(i))
    dic = dict()
    for j in range(i):
        dic[j] = j
    dic = dict(zip(range(100001), range(100001)))

    lg = list_get.timeit(number=1000)
    dg = dict_get.timeit(number=1000)
    ds = dict_set.timeit(number=1000)
    ld = list_del.timeit(number=1000)
    dd = timeit.timeit('del dic[5000]', 'dic = dict(zip(range(100001), range(100001)))', number=1000)
    print('%10.6f,%10.6f,%10.6f,%10.6f,%10.6f' % (lg, dg, ds, ld, dd))

