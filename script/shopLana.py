from .baseNPC import BaseNPC

class ShopLana(BaseNPC):
    """拉娜的商店，提供寶石交易和服裝製作功能"""
    def __init__(self, player):
        super().__init__(player, name="拉娜", role="服裝設計師")
        
    def get_initial_dialogue(self):
        return [
            "\n**綠髮精靈**：「你就是傳說中的人類嗎？我是拉娜，是一名服裝設計師。」",
            "**拉娜**：「你初來乍到的，服裝習慣和我們很不同呢。」",
            "**拉娜**：「好的服裝可以降低因為污染生病的風險。」",
            "**拉娜**：「假如你的身上有生物掉落物我可以收購哦~」"
        ]
    
    def get_repeat_dialogue(self):
        return ["**拉娜**：「假如你的身上有生物掉落物我可以收購哦~」"]
    
    def handle_interaction(self):
        """處理商店互動"""
        # 顯示對話
        if self.gossip == 0:
            for line in self.get_initial_dialogue():
                print(line)
        else:
            for line in self.get_repeat_dialogue():
                print(line)
                
        # 解鎖商店功能
        if self.unlock_feature("shop"):
            print("✨ 你解鎖了 **寶石交易 & 衣服 製作功能**！")
        else:
            print("💎 你可以與拉娜交易寶石或製作衣服飾品。")
            
        self.gossip += 1
    
    def shop(self):
        """原有的商店功能保持不變，但現在透過 handle_interaction 調用"""
        self.handle_interaction()