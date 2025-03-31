def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("0で割ることはできません")
    return x / y

def main():
    print("シンプル電卓")
    print("1. 足し算")
    print("2. 引き算")
    print("3. 掛け算")
    print("4. 割り算")
    
    while True:
        choice = input("操作を選択してください (1/2/3/4): ")
        
        if choice not in ['1', '2', '3', '4']:
            print("無効な選択です。もう一度お試しください。")
            continue
            
        num1 = float(input("1つ目の数字を入力してください: "))
        num2 = float(input("2つ目の数字を入力してください: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
                
        next_calculation = input("もう一度計算しますか？ (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    
    print("ご利用ありがとうございました！")

if __name__ == "__main__":
    main() 