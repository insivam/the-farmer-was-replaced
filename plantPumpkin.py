def plantPumpkin(plant_amount=10):
    for times in range(plant_amount):
        world_size = get_world_size()
        
        positions_not_planted = []
        for x in range(world_size):
            for y in range(world_size):
                positions_not_planted.append([x, y])
        
        while positions_not_planted:
            for pos in positions_not_planted[:]:
                pos_x, pos_y = pos
                if pos != [get_pos_x(), get_pos_y()]:
                    moveTo(pos_x, pos_y)
                else:
                    trade(Items.Fertilizer)
                    use_item(Items.Fertilizer)
                
                if get_ground_type() != Grounds.Soil:
                    till()
                
                if get_entity_type() != Entities.Pumpkin:
                    harvest()
                    trade(Items.Pumpkin_Seed)
                    plant(Entities.Pumpkin)
                    
                if can_harvest():
                    positions_not_planted.remove(pos)
                
                if get_water() < 0.75:
                    use_item(Items.Water_Tank)
        harvest()