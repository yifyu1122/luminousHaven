def breed_creatures(player, index1, index2):
    """讓兩隻魔法生物繁殖，依照品種需求不同資源
    
    Args:
        player: Player 實例，用於存取資源和生物清單
        index1: 第一隻父本生物的索引
        index2: 第二隻父本生物的索引
    """
    if len(player.inventory) >= player.max_creatures:
        player.list_creatures()
        print("❌ 培育室已滿，無法進行繁殖！請先釋放或合併生物。")           
        print("💡 提示：請使用 `merge A B` 來融合生物，以釋放空間！")
        return

    # 確保輸入的索引是有效的
    if index1 < 1 or index2 < 1 or index1 > len(player.inventory) or index2 > len(player.inventory):
        print("❌ 無效的生物編號！")
        return

    parent1 = player.inventory[index1 - 1]
    parent2 = player.inventory[index2 - 1]

    # **確保名稱統一後再比對**
    parent1_name = parent1.name.strip()
    parent2_name = parent2.name.strip()

    print(f"🐣 嘗試繁殖：{parent1_name}（{parent1.color}） 和 {parent2_name}（{parent2.color}）")

    if parent1_name != parent2_name:
        print(f"❌ {parent1_name} 和 {parent2_name} 不是同品種，無法繁殖！")
        return

    # **根據品種決定繁殖所需資源**
    if parent1_name == "星光螢火蟲":
        required_resources = ["螢露蜜", "螢露土", "螢露水"]
    elif parent1_name == "夢魘貓":
        required_resources = ["夢魘果實", "夢魘之塵", "夢魘精華"]
    else:
        print(f"❌ {parent1_name} 目前無法繁殖！")
        return

    # **檢查是否擁有足夠的繁殖資源**
    missing_resources = [res for res in required_resources if player.resources.get(res) < 1]

    if missing_resources:
        print(f"❌ 無法繁殖！缺少以下資源：{', '.join(missing_resources)}")
        return

    # 修改資源消耗方式
    child = parent1.breed(parent2, player)

    if child:
        # 使用 ResourceManager 的 consume 方法
        for res in required_resources:
            player.resources.consume(res)

        player.inventory.append(child)
        print(f"🍼 {child.name}（{child.color}） 誕生了！你已消耗 1 份「{'、'.join(required_resources)}」。")