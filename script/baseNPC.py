class BaseNPC:
    def __init__(self, player, name, role):
        self.player = player
        self.name = name
        self.role = role
        self.gossip = 0
        
    def get_initial_dialogue(self):
        """獲取初次對話內容，子類需要重寫這個方法"""
        raise NotImplementedError
        
    def get_repeat_dialogue(self):
        """獲取重複對話內容，子類需要重寫這個方法"""
        raise NotImplementedError
        
    def handle_interaction(self):
        """處理互動，子類需要重寫這個方法"""
        raise NotImplementedError
        
    def unlock_feature(self, feature_name):
        """解鎖特定功能"""
        if not self.player.village.unlocked_features[feature_name]:
            self.player.village.unlocked_features[feature_name] = True
            return True
        return False