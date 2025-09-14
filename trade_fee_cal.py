#비트코인 수수료 계산기 및 레버리지 수수료
seed = float(input("투자 금액을 단위: 만 으로 입력해주세요 \n 예시)1만5천원->1.5 : "))
print("코인 거래소를 선택하세요. 선택에 따라 기본 수수료값이 설정됩니다. \n 1.바이낸스 \n 2.빗썸")
market = int(input("번호를 입력해주세요 : "))

if market == 1:
    normal_fee = 0.08
    str(market)
    market="바이낸스 선물거래 기준"
elif market == 2:
    normal_fee = 0.04
    str(market)
    market="빗썸"
#0이하의 수를 퍼센트화 하는 식
normal_fee = normal_fee/100

print("%s (으)로 설정되었습니다. "%market)
leverage = int(input("레버리지 설정값을 입력해주세요 \n 예시) 10배->10  : "))
direction = int(input("포지션 선택 \n 1. 롱(매수)\n 2. 숏(매도)"))
if direction == 1:
    add='+'
elif direction == 2:
    add='-'
position_size = seed*leverage
lev_fee = seed*normal_fee*leverage/100
trade_fee = position_size*normal_fee
funding_fee = 0.01/100*position_size
all_fee = trade_fee+funding_fee
profit = all_fee*1/seed*100
print("총 이용 수수료 : %.1f만원입니다."%all_fee)
if direction == 1:
    print("투자금 : %.1f만원의 수익이 생기는 지점은 %s%.1f%%부터입니다."%(seed,add,profit))
elif direction == 2:
    print("투자금 : %.1f만원의 수익이 생기는 지점은 ROI: %s%.1f%%부터입니다."%(seed,add,profit))
