def merge_creatures(player, index1, index2): 
        """讓兩隻魔法生物合體，提升主體能量，但不直接進化"""
        
        # 確保輸入的索引是有效的
        if index1 < 1 or index2 < 1 or index1 > len(player.inventory) or index2 > len(player.inventory):
            print("❌ 無效的生物編號！")
            return

        if index1 == index2:
            print("❌ 不能自己跟自己合體！")
            return

        # 取得兩隻生物
        creature1 = player.inventory[index1 - 1]
        creature2 = player.inventory[index2 - 1]

        # 確保品種相同
        if creature1.name != creature2.name:
            print(f"❌ {creature1.name} 和 {creature2.name} 不是同品種，無法合體！")
            return

        # 確保顏色相同
        if creature1.color != creature2.color:
            print(f"❌ {creature1.name}（{creature1.color}） 和 {creature2.name}（{creature2.color}） 顏色不同，無法合體！")
            return

        # 執行合體強化
        print(f"⚡ {creature1.name}（{creature1.color}） 吞噬了 {creature2.name}（{creature2.color}）！")
        
        # 增加能量 #
        creature1.energy += min(creature2.energy * 0.2, 10)
        creature1.energy_rate += min(creature2.energy * 0.2, 10)  

        print(f"🔥 {creature2.name}（{creature2.color}） 被吞噬，從庫存中移除！")
        player.inventory.remove(creature2)

        print(f"✅ {creature1.name}（{creature1.color}） 吞噬後獲得力量，能量提升至 {creature1.energy}，產能提升至 {creature1.energy_rate:.1f}！")