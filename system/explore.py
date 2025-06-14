import time
import random
from system.village import Village
def explore(player, location="螢露谷"):
    """探索螢露谷或夢魘灣，獲得不同的資源或魔法生物"""
    if len(player.inventory) >= player.max_creatures:
        player.list_creatures()
        print("❌ 培育室已滿，無法進行探索！請先釋放或合併生物。")           
        print("💡 提示：請使用 `merge A B` 來融合生物，以釋放空間！")
        return
    
    if location not in ["螢露谷", "夢魘灣", "精靈部落"]:
        print("❌ 無效的探索地點！請選擇 `螢露谷` 或 `夢魘灣`")
        return

    if player.polluted_lands[location]:
        print(f"❌ {location} 已被汙染，無法探索！請使用七彩寶石進行淨化。")
        return

    # 夢魘灣只有當玩家解鎖第一塊土地後才可探索
    if location == "夢魘灣" and player.unlocked_lands < 1:
        print("❌ 你尚未解鎖「夢魘灣」！請先使用七彩寶石解鎖土地。")
        return  
    
    # 精靈部落只有當玩家解鎖第一塊土地後才可探索
    if location == "精靈部落" and player.unlocked_lands < 1:
        print("❌ 你尚未解鎖「精靈部落」！請先使用七彩寶石解鎖土地。")
        village = Village()  
        village.enter()
        return

    print(f"🛤️ 你開始探索 {location}... ⏳（需時 1:00）")
    time.sleep(3)  # 模擬探索時間（縮短為 3 秒）

    # 探索獎勵
    if location == "螢露谷":
        rewards = ["螢露蜜", "螢露土", "螢露水"]
        special_creature_name = "星光螢火蟲"
        special_creature_colors = ["綠", "藍", "紫"]
        special_creature_chance = 0.3
        # **每次探索必定獲得 3 種基礎資源**
        for reward in rewards:
            player.resources.add(reward)
        print(f"🎉 你成功探索 {location}，獲得了 **螢露蜜、螢露土、螢露水**！")
    elif location == "夢魘灣":
        rewards = ["夢魘果實", "夢魘之塵", "夢魘精華"]
        special_creature_name = "夢魘貓"
        special_creature_colors = ["橙", "黃", "紫"]
        special_creature_chance = 0.3
        for reward in rewards:
            player.resources.add(reward)
        print(f"🎉 你成功探索 {location}，獲得了 **夢魘果實、夢魘之塵、夢魘精華**！")


    # 可能遇到特殊生物
    if random.random() < special_creature_chance:
        new_color = random.choice(special_creature_colors)
        # 確保名稱統一
        normalized_creature_name = special_creature_name.strip()
        player.add_creature(normalized_creature_name, new_color)
        print(f"✨ 你在探索中遇見了一隻 **{new_color} 色的 {normalized_creature_name}**，並成功帶回培育室！✨")

    player.exploration_count[location] += 1
    print(f"🔍 {location} 已探索 {player.exploration_count[location]} 次。")

    if player.exploration_count[location] % 50 == 0:
        player.polluted_lands[location] = True
        print(f"⚠️ {location} 已被汙染，無法再探索！請使用七彩寶石進行淨化。")

    # 離開期間生物會產生能量
    for creature in player.inventory:
        creature.energy += creature.energy_rate
        print(f"🔋 {creature.name}（{creature.color}） 產生了 {creature.energy_rate} 點能量！")

        for creature in player.inventory:
            drops = creature.drop_gem()
            for item in drops:
                player.resources.add(item)
                print(f"🌟 你現在擁有 {player.resources.get(item)} 個 {item}！")