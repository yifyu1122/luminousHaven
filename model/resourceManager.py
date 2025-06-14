class ResourceManager:
    def __init__(self):
        self.resources = {
            "螢露蜜": 0,
            "螢露土": 0,
            "螢露水": 0,
            "夢魘果實": 0,
            "夢魘之塵": 0,
            "夢魘精華": 0,
            "星輝之粉": 0,
            "夢魘貓毛": 0, 
            "七彩寶石": 0,
            "紅寶石": 0,
            "橙寶石": 0,
            "黃寶石": 0,
            "綠寶石": 0,
            "藍寶石": 0,
            "紫寶石": 0,
            "透明寶石": 0,
            "精靈幣": 0
        }

    def add(self, item, amount=1):
        self.resources[item] = self.resources.get(item, 0) + amount

    def consume(self, item, amount=1):
        if self.resources.get(item, 0) >= amount:
            self.resources[item] -= amount
            return True
        else:
            return False

    def get(self, item):
        return self.resources.get(item, 0)

    def list_resources(self):
        """顯示玩家持有的所有資源"""
        # 過濾出數量大於 0 的資源
        owned_resources = {k: v for k, v in self.resources.items() if v > 0}

        if not owned_resources:
            print("❌ 你目前沒有任何資源！")
            return {}

        print("\n🔹 你的資源：")
        for resource, count in owned_resources.items():
            print(f"   {resource}：{count}")
            
        return owned_resources  # 返回資源字典，以便其他方法使用
