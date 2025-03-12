import village

class plantLuna:
    def __init__(self):
        self.gossip = 0
    def plant(self):
        print("\n🌿 **露娜**：「你喜歡植物嗎？這裡有許多珍貴的魔法種子。」")
        if not village.unlocked_features["greenhouse"]:
            village.unlocked_features["greenhouse"] = True
            print("✨ 你解鎖了 **溫室功能**，可以種植特殊植物！")
        else:
            print("🌱 你可以向露娜學習如何培育魔法植物。")