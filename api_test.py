'''import requests

url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberCurrStateList'
params = {'serviceKey': 'ZFXmFX0IXF2lZtUXaZW+lLjQUBH3AFz14p6BfEC8AFWev/Xplh7PYsaHYzPkqXnMJ03TJbhvS4jBYA2aRNAglQ==', 'numOfRows' : '10', 'pageNo' : '1' }

response = requests.get(url, params=params)
print(response.content)
'''
'''
import os
import sys
import urllib.request

client_id = "NrkKI0dzkjbVyJJaGGg1"
client_secret = "bxP7XUH_Sh"    
encText = urllib.parse.quote("사랑")
url = "https://openapi.naver.com/v1/search/book.xml?display=10&start=1&query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
'''
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import spam

client_id = "haTmx_2L7UB1bo68x0d8"
client_secret = "Zf0wkFCKHv"
encText = urllib.parse.quote("미국 국기 jpg")
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
url = "https://openapi.naver.com/v1/search/image.xml?query=" + encText + "&display=10&sort=sim"# xml

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

