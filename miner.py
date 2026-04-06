# ========== 图图链核心：全网统一规则 ==========
GENESIS_HASH = "TUTU_CHAIN_20260406"  # 你定的创世标识
GENESIS_CHAR = "图"

# 所有人必须用这套一模一样的算法！
# 只要改一个字符，就是另一条链
def mine():
    k = 0
    print("🚀 图图链公链挖矿开始（全网统一链）")
    while True:
        code = ord(GENESIS_CHAR)
        cond1 = (code + k) % 26
        cond2 = (code * k) % 36
        if cond1 == 12 and cond2 == 18:
            print(f"\n✅ 出块成功！K={k}")
            print("💰 奖励 50 TUTU（图图公链）")
            return
        k += 1
        if k % 100000 == 0:
            print(f"尝试 K={k}...")

if __name__ == "__main__":
    mine()