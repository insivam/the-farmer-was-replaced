def calcMaxSunflower(all_sunflowers):
    max_petals = all_sunflowers[0][0]
    all_max_petals = [[all_sunflowers[0][1], all_sunflowers[0][2]]]
    for flower in all_sunflowers[1:]:
        if flower[0] > max_petals:
            max_petals = flower[0] 
            all_max_petals = [[flower[1], flower[2]]]
        elif flower[0] == max_petals:
            all_max_petals.append([flower[1], flower[2]])
    return all_max_petals

def plantSunflower(plant_amount=100):
    count_sunflower = 0
    all_sunflowers = []
    while count_sunflower < plant_amount:
        if get_ground_type() != Grounds.Soil:
            till()

        current_x, current_y = get_pos_x(), get_pos_y()
        
        all_done = len(all_sunflowers) == get_world_size()**2
        removed = False
        if all_done:
            max_sunflowers = calcMaxSunflower(all_sunflowers)
            while True:
                for flower in max_sunflowers:                        
                    if [current_x, current_y] != [flower[0], flower[1]]:
                        moveTo(flower[0], flower[1])
                        current_x, current_y = get_pos_x(), get_pos_y()
                    else:
                        trade(Items.Fertilizer)
                        use_item(Items.Fertilizer)
                    if can_harvest():
                        all_sunflowers.remove([measure(), current_x, current_y])
                        removed = True
                        
                        harvest()
                    
                        trade(Items.Sunflower_Seed)
                        count_sunflower += 1
                        plant(Entities.Sunflower)

                        if get_water() < 0.75:
                            use_item(Items.Water_Tank)                
                        all_sunflowers.append([measure(), current_x, current_y])
                    if removed:
                        break
                if removed:
                    break
        if get_entity_type() != Entities.Sunflower:
            harvest()
            trade(Items.Sunflower_Seed)
            plant(Entities.Sunflower)
        elif not all_done:
            all_sunflowers.append([measure(), current_x, current_y])
            
        if not all_done:
            move(North)
            if current_y == 0:
                move(East)
                