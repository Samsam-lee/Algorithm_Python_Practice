def BigNumber(data):
    # print(data[0], data[1], data[2])
    print(data)
    



print('몇개의 수, 총 더하는 횟수, 특정 인덱스의 숫자가 연속해서 더해질 수 있는 횟수\n띄어쓰기를 하고 입력해주세요.')
temp1, temp2, temp3 = map(int, input().split())

print(temp1, '개의 수를 입력 해 주세요')
data = list(map(int, input().split()))
data.sort()


BigNumber(data)
