class shopLana:
    def __init__(self, player):
        self.gossip = 0
        self.player = player
    def shop(self):
        if self.gossip == 0:
            print("\n**綠髮精靈**：「你就是傳說中的人類嗎？我是拉娜，是一名服裝設計師。」")            
            print("**拉娜**：「你初來乍到的，服裝習慣和我們很不同呢。」")
            print("**拉娜**：「好的服裝可以降低因為污染生病的風險。」")
            print("**拉娜**：「假如你的身上有生物掉落物我可以收購哦~」")
        else:
            print("**拉娜**：「假如你的身上有生物掉落物我可以收購哦~」")
            
        if not self.player.village.unlocked_features["shop"]:
            self.player.village.unlocked_features["shop"] = True
            print("✨ 你解鎖了 **寶石交易 & 衣服 製作功能**！")
        else:
            print("💎 你可以與拉娜交易寶石或製作衣服飾品。")
        self.gossip += 1