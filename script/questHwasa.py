from .baseNPC import BaseNPC

class QuestHwasa(BaseNPC):
    def __init__(self, player):
       super().__init__(player, name="華莎", role="村長")

    def get_initial_dialogue(self):
        return [
            "\n你走到了那位銀髮精靈面前。",
            "**銀髮精靈**：「我是這個部落的村長華莎，叫我華莎就好了。」",
            "**華莎**：「你對這個世界了解多少呢？」",
            "**華莎**：「這個世界原本由三大種族主宰，精靈主宰天空、人類主宰著地面、人魚主宰海洋。」",
            "**華莎**：「你或許是世間僅存的唯一人類了。」"
            "**華莎**：「末日發生後，我們精靈被剝奪飛行的能力，墜落地面。」",
            "**華莎**：「通訊被汙染，我們與海洋及其他部落失去聯繫。」",
            "**華莎**：「人類阿...假如可以的話，幫我聯繫到其他部落就好了。」"
        ]
    
    def get_repeat_dialogue(self):
        return [
            "\n**華莎**：「你好，人類！有什麼需要幫忙的嗎？」",
            "**華莎**：「如果你需要任務或資訊，隨時可以來找我。」"
        ]     
        
    def handle_interaction(self):
        """處理與華莎的互動"""    
        if self.gossip == 0:
            for line in self.get_initial_dialogue():
                print(line)
        else:
            for line in self.get_repeat_dialogue():
                print(line)

        if self.unlock_feature("quests"):
            print("✨ 你解鎖了 **任務系統**，可以接受華莎的任務！")
        else:
            print("🔍 你可以向華莎接受任務，完成任務可以獲得獎勵。")

        self.gossip += 1
            