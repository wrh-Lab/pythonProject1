import urllib.error
import urllib.request
from audioop import error

url="http://www.baidu.com"
try:
    response=urllib.request.urlopen(url)
except error.URLError as e:
    print(e.reason)