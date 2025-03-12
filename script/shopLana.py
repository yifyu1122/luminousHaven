import village

class shopLana:
    def __init__(self):
        self.gossip = 0
    def shop(self):
        print("\n🛍️ **拉娜**：「你好！我收購寶石、毛皮，也可以幫你做飾品哦！」")
        if not village.unlocked_features["shop"]:
            village.unlocked_features["shop"] = True
            print("✨ 你解鎖了 **寶石交易 & 飾品製作功能**！")
        else:
            print("💎 你可以與拉娜交易寶石或製作飾品。")