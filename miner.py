import random
from wallet import Wallet

def load_char_data():
    data = []
    with open("char_data.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            code, initial, stroke = line.split(",")
            data.append((int(code), initial, int(stroke)))
    return data

def mine():
    data = load_char_data()
    wallet = Wallet()

    code, initial, stroke = random.choice(data)
    char = chr(code)
    reward = 1

    wallet.add(reward)

    print(f"挖到：{char}")
    print(f"编码：{code} 首字母：{initial} 笔画：{stroke}")
    print(f"+{reward} | 余额：{wallet.get_balance()}")

if __name__ == "__main__":
    mine()