# 종목/수량/평단 , 판매가
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]


def stock_profit(stocks, sells):
    results = []
    stock_list = stocks.split(",")

    # 종목별 수익률 튜플을 리스트에 저장
    for i, stock in enumerate(stock_list):

        [name, _, buy_price] = stock.split("/")

        performance = (sells[i] - int(buy_price)) / int(buy_price) * 100

        results.append((name, performance))

    # 수익률 기준 역정렬 후 출력
    for name, performance in sorted(results, key=lambda x: x[1], reverse=True):
        print(f"{name}의 수익률 {performance:.3}")


stock_profit(stocks, sells)
