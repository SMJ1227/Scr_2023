'''
import urllib
import http.client

conn = http.client.HTTPConnection("apis.data.go.kr")
conn.request("GET","/B551182/hospInfoServicev2/getHospBasisList?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&pageNo=1&numOfRows=10&sidoCd=110000&sgguCd=110019")
req = conn.getresponse()
print(req.status, req.reason)
print(req.read().decode('utf-8'))
'''
'''
import requests
import xml.etree.ElementTree as ET
import tkinter

#기상청 동네예보 통보문 조회서비스
url = 'http://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation'
# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key_weather = "ZFXmFX0IXF2lZtUXaZW+lLjQUBH3AFz14p6BfEC8AFWev/Xplh7PYsaHYzPkqXnMJ03TJbhvS4jBYA2aRNAglQ=="
queryParams_weather = {'ServiceKey': service_key_weather, 'pageNo': '1', 'numOfRows': '10', 'dataType': 'XML', 'stnId': '108'}

response_weather = requests.get(url, params=queryParams_weather)
print(response_weather.content)
root = ET.fromstring(response_weather.content)

window = tkinter.Tk()
window.title('기상개황조회')

frame = tkinter.Frame(window)
frame.pack()

header = ['stnId', 'tmFc', 'wfSv1', 'wn', 'wr']

for i, col_name in enumerate(header):
    label = tkinter.Label(frame, text=col_name, font=("Helvetica", 14, "bold"), borderwidth=1, relief="raised")
    label.grid(row=i, column=0)

col_count = 1
for item in root.iter('item'):
    stnId = item.findtext('stnId')
    tmFc = item.findtext("tmFc")
    wfSv1 = item.findtext("wfSv1")
    wn = item.findtext("wn")
    wr = item.findtext("wr")
    data = [stnId, tmFc, wfSv1, wn, wr]
    for i, value in enumerate(data):
        label = tkinter.Label(frame, text=value, font=("Helvetica", 12), borderwidth=10, relief="ridge")
        label.grid(row=i, column=col_count)
    col_count += 1

window.mainloop()
'''
'''
# folium 지도  띄우기
from tkinter import *
import folium
import webbrowser
def pressed():
    map_osm = folium.Map(location=[37.3402849, 126.7313189], zoom_start=13)
    folium.Marker([37.3402849, 126.7313189], popup='한국공학대학교').add_to(map_osm)
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

window = Tk()
window.geometry('600x400')
Button(window, text='folium 지도', command=pressed).pack()
window.mainloop()
'''


#notebook 예제
from tkinter import *
import tkinter.ttk
import requests
import xml.etree.ElementTree as ET

#기상청 동네예보 통보문 조회서비스
url = 'http://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation'
# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key_weather = "ZFXmFX0IXF2lZtUXaZW+lLjQUBH3AFz14p6BfEC8AFWev/Xplh7PYsaHYzPkqXnMJ03TJbhvS4jBYA2aRNAglQ=="
queryParams_weather = {'ServiceKey': service_key_weather, 'pageNo': '1', 'numOfRows': '10', 'dataType': 'XML', 'stnId': '108'}

response_weather = requests.get(url, params=queryParams_weather)
print(response_weather.content)
root = ET.fromstring(response_weather.content)


window = Tk()
window.title('tkinter notebook')
notebook = tkinter.ttk.Notebook(window, width=800, height=600)
notebook.pack()

frame1 = Frame(window)
notebook.add(frame1, text='페이지1')
header = ['stnId', 'tmFc', 'wfSv1', 'wn', 'wr']

for i, col_name in enumerate(header):
    label = tkinter.Label(frame1, text=col_name, font=("Helvetica", 14, "bold"), borderwidth=1, relief="raised")
    label.grid(row=i, column=0)

col_count = 1
for item in root.iter('item'):
    stnId = item.findtext('stnId')
    tmFc = item.findtext("tmFc")
    wfSv1 = item.findtext("wfSv1")
    wn = item.findtext("wn")
    wr = item.findtext("wr")
    data = [stnId, tmFc, wfSv1, wn, wr]
    for i, value in enumerate(data):
        label = tkinter.Label(frame1, text=value, font=("Helvetica", 12), borderwidth=10, relief="ridge")
        label.grid(row=i, column=col_count)
    col_count += 1

frame2 = Frame(window)
notebook.add(frame2, text='페이지2')
Label(frame2, text='페이지2의 내용', fg='yellow', font='helvetica 48').pack()

frame3 = Frame(window)
notebook.add(frame3, text='페이지3')
Label(frame3, text='페이지3의 내용', fg='green', font='helvetica 48').pack()

frame4 = Frame(window)
notebook.add(frame4, text='페이지4')
Label(frame4, text='페이지4의 내용', fg='blue', font='helvetica 48').pack()

window.mainloop()