'''
import urllib
import http.client

conn = http.client.HTTPConnection("apis.data.go.kr")
conn.request("GET","/B551182/hospInfoServicev2/getHospBasisList?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&pageNo=1&numOfRows=10&sidoCd=110000&sgguCd=110019")
req = conn.getresponse()
print(req.status, req.reason)
print(req.read().decode('utf-8'))
'''

import requests
import xml.etree.ElementTree as ET
import tkinter

#병원정보 서비스 예제
url = 'http://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList'
# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key = "sea100UMmw23Xycs33F1EQnumONR/9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw=="
queryParams = {'serviceKey': service_key, 'pageNo': '1', 'numOfRows': '10', 'sidoCd': '110000', 'sgguCd': '110019'}

response = requests.get(url, params=queryParams)
print(response.text)
root = ET.fromstring(response.text)

window = tkinter.Tk()
window.title('병원정보')

frame = tkinter.Frame(window)
frame.pack()

header = ['Name', 'Addr', 'Tel', 'Url']

for i, col_name in enumerate(header):
    label = tkinter.Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
    label.grid(row=0, column=i)

row_count = 1
for item in root.iter('item'):
    yadmNm = item.findtext('yadmNm')
    addr = item.findtext("addr")
    telno = item.findtext("telno")
    hospUrl = item.findtext("hospUrl")
    data = [yadmNm, addr, telno, hospUrl]
    for i, value in enumerate(data):
        label = tkinter.Label(frame, text=value, font=("Helvetica", 12))
        label.grid(row=row_count, column=i)

    row_count += 1

window.mainloop()

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

'''
#notebook 예제
from tkinter import *
import tkinter.ttk

window = Tk()
window.title('tkinter notebook')
notebook = tkinter.ttk.Notebook(window, width=800, height=600)
notebook.pack()

frame1 = Frame(window)
notebook.add(frame1, text='페이지1')
Label(frame1, text='페이지1의 내용', fg='red', font='helvetica 48').pack()

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
'''