class questHwasa:
    def __init__(self, player):
       self.gossip = 0
       self.player = player
       
    def quest(self):
        if self.gossip == 0:
            print("\n你走到了那位銀髮精靈面前。")
            print("**銀髮精靈**：「我是這個部落的村長華莎，叫我華莎就好了。」")
            print("**華莎**：「你對這個世界了解多少呢？」")
            print("**華莎**：「這個世界原本由三大種族主宰，精靈主宰天空、人類主宰著地面、人魚主宰海洋。」")
            print("**華莎**：「你或許是世間僅存的唯一人類了。」")
            print("**華莎**：「末日發生後，我們精靈被剝奪飛行的能力，墜落地面。」")
            print("**華莎**：「通訊被汙染，我們與海洋及其他部落失去聯繫。」")
            print("**華莎**：「人類阿...假如可以的話，幫我聯繫到其他部落就好了。」")            
        else:
            print("\n**華莎**：「你好，人類！我有一個任務需要你的幫助。」")

        if not self.player.village.unlocked_features["quests"]:
            self.player.village.unlocked_features["quests"] = True
            print("✨ 你解鎖了 **任務系統**，可以接受華莎的任務！")
        else:
            print("🔍 你可以向華莎接受任務，完成任務可以獲得獎勵。")

        self.gossip += 1
            