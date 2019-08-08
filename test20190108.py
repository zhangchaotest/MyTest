# 基础方法


# 增加cache

def fnc(n, cache=None):
    if n <= 2:
        return 1
    if cache == None:
        cache = {}
    if n in cache:
        return cache[n]
    cache[n] = fnc(n - 1, cache=cache) + fnc((n - 2), cache=cache)
    return cache[n]


# 装饰器

def fn_cache(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@fn_cache
def fn(n):
    if n <= 2:
        return 1
    return fn(n - 2) + fn(n - 1)


print(fn(100))
print(fnc(100))
