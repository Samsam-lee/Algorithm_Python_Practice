items=[(1,5,20), (2,10,10), (3,7,6), (4,7,5)]
selected=[]
m=20

#문제에서 무게당 이익 순으로 데이터를 줄 경우 정렬 과정은 생략해도 된다.
sorted-item=sorted(items, key=lambda items:items[2]/items[1], reverse=True)

while m > 0 and len(items) > 0:
    i=items[0][0]
    wi=items[0][1]
    pi=items[0][2]
    rate=1
    if wi > m:
        rate=m/wi
    items=(i,wi*rate, pi*rate)
    selected.append(item)
    del items[0]
    m=m-wi*rate

print(selected)