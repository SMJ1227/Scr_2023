sales = 25000000
commission = 0
while True:
    if (commission+sales) >= 30000000:
        print("연봉 3천만원이 되기 위한 최소 금액은 ", sales)
        break
    else:
        sales += 1
        print(sales, commission)
        if sales >= 10000001:
            commission = 5000000*0.08 + 5000000*0.1 + (sales - 10000000)*0.12
        elif sales >= 5000001:
            commission = 5000000 * 0.08 + (sales - 5000000) * 0.1
        else:
            commission = sales * 0.08
