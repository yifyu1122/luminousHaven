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
        """消耗指定數量的資源"""
        if self.resources.get(item, 0) >= amount:
            self.resources[item] -= amount
            return True
        return False

    def get(self, item):
        """獲取指定資源的數量"""
        return self.resources.get(item, 0)


