
import account


def main():
    chiedu = account.Account("chiedu", "chichi", 200000)
    nicki = account.Account("Nicki", "Nikoli", 20000)
    james = account.Account("James", "JimmyB", 210)
    chiedu.deposit(200000)
    chiedu.withdraw(20)
    chiedu.deposit(20)
    chiedu.withdraw(209)
    print(chiedu)
    nicki.deposit(2000)
    nicki.withdraw(105)
    nicki.deposit(200)
    nicki.withdraw(20)
    print(nicki)
    james.deposit(10)
    james.withdraw(30)
    james.deposit(50)
    if james.withdraw(250):
        print(james)
    else:
        print("insufficient funds")

main()
