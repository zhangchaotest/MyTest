import requests
def send_reqyest(url):
    r = requests.get(url)
    return r.status_code

def visit_ustack():
    return send_reqyest("http://www.ustack.com")