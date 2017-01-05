from urllib.error import *
from urllib.request import *
import re

url = "http://www.proxy360.cn/default.aspx"
try:
    request = Request(url)
    response=urlopen(request)
    #print(response.read())
    content=response.read().decode('UTF-8')
    pattern = re.compile(' <span .*?140px;">\s+(.*?)\s+</span>\s+<span .*?50px;">\s+(.*?)\s+</span>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print(item)
except URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
