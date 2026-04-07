import json
import os

WALLET_FILE = "wallet_data.json"

class Wallet:
    def __init__(self):
        self.balance = 0
        self._load()

    def _load(self):
        if os.path.exists(WALLET_FILE):
            with open(WALLET_FILE, "r", encoding="utf-8") as f:
                self.balance = json.load(f).get("balance", 0)
        else:
            self.balance = 0
            self._save()

    def _save(self):
        with open(WALLET_FILE, "w", encoding="utf-8") as f:
            json.dump({"balance": self.balance}, f)

    def add(self, amount):
        self.balance += amount
        self._save()

    def get_balance(self):
        return self.balance


# 👇 只显示钱包余额，干净中文，没有挖矿信息
if __name__ == "__main__":
    wallet = Wallet()
    print(f"【钱包】当前余额：{wallet.get_balance()}")