def open_account(a):
    print("{}님 새로운 계좌가 생성되었습니다.".format(a))

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance , money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

def main():
    open_account("이동헌")
    balance = 0
    balance = deposit(balance, 1000)
    # balance = withdraw(balance, 2000)
    # balance = withdraw(balance, 500)
    commission, balance = withdraw_night(balance, 500)
    print("수수료는 {0}원이고, 잔액은 {1}원입니다.".format(commission, balance))

main()