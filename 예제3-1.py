#카운트 0으로 스타트
n=int(input('금액을 입력하세요: '))
count=0
#카운트에 점차 몫을 더하고 n은 갱신해야됨+반복문 사용
coin_types=[500,100,50,10]
for coin in coin_types:
    count=count+n//coin
    n=n%coin
print(f'개수는 {count}개 입니다.')




























