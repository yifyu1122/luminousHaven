import village

class questHwasa:
    def __init__(self):
       self.gossip = 0
       
    def quest(self):
        #我們的祖先曾經有過翅膀，住在空中的島嶼。隨著汙染的擴散，我們的翅膀已經退化了。
        print("\n🌟 **華莎**：「你好，冒險者！我有一個任務需要你的幫助。」")
        if not village.unlocked_features["quest"]:
            village.unlocked_features["quest"] = True
            print("✨ 你解鎖了 **任務系統**，可以接受華莎的任務！")
        else:
            print("🔍 你可以向華莎接受任務，完成任務可以獲得獎勵。")