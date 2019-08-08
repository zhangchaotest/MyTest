def fn(n):
    if n <= 2:
        return 1
    return fn(n - 1) + fn(n - 2)


def fn_cache(n, cache=None):
    if cache is None:
        cache = {}
    if n < 2:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fn_cache(n - 1, cache) + fn_cache(n - 2, cache)
    return cache[n]

    if __name__ == '__main__':
        print(fn(5))
