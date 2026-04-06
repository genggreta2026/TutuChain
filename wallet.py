# TutuChain 图图链钱包 - 创世版
import hashlib

# 创世标识（只有这个链的钱包有效）
GENESIS_SEED = "TUTU_CHAIN_20260406_图"

def generate_wallet():
    # 生成私钥
    private_key = hashlib.sha256(GENESIS_SEED.encode()).hexdigest()
    # 生成地址
    address = "TU" + hashlib.md5(private_key.encode()).hexdigest()[:16]
    
    print("💰 图图链钱包生成成功！")
    print(f"地址: {address}")
    print(f"私钥: {private_key}")
    print("⚠️  私钥请保密！丢失无法找回！")

if __name__ == "__main__":
    generate_wallet()