import requests


# class ygRequest(requests):
#     pass
# a=ygRequest()
res = requests.get(url='https://b.faloo.com/l/0/1.html?t=1&k=%CB%D9%B6%C8')
print(res.text)
