import requests

url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberCurrStateList'
params = {'serviceKey': 'ZFXmFX0IXF2lZtUXaZW+lLjQUBH3AFz14p6BfEC8AFWev/Xplh7PYsaHYzPkqXnMJ03TJbhvS4jBYA2aRNAglQ==', 'numOfRows' : '10', 'pageNo' : '1' }

response = requests.get(url, params=params)
print(response.content)
