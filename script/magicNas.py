import village 

class magicNas:
    def __init__(self):
        self.gossip = 0
    def magic(self):
        print("\n🔮 **娜絲**：「你的魔法能量不夠強大，這樣沒辦法對抗污染！」")
        if not village.unlocked_features["magic"]:
            village.unlocked_features["magic"] = True
            print("✨ 你解鎖了 **魔法學習功能**，可以提升淨化等級！")
        else:
            print("📖 你可以向娜絲學習更多魔法來增強自己的能力。") 