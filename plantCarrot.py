def plantCarrot(plant_amount=10):
    moveTo(0, 0)
    for i in range(plant_amount):
        while True:
            if get_ground_type() != Grounds.Soil:
                till()
            if can_harvest():
                harvest()
            trade(Items.Carrot_Seed)
            plant(Entities.Carrots)
            
            if get_water() < 0.75:
                use_item(Items.Water_Tank)
        
            move(North)
            if get_pos_y() == 0:
                move(East)
            if [get_pos_x(), get_pos_y()] == [0, 0]:
                break
                