def should_plant_tree(current_x, current_y, ground):
    if (current_y % 2 == 0 and current_x % 2 == 1) or (current_y % 2 == 1 and current_x % 2 == 0):
        if ground == Grounds.Turf:
            till()
        plant(Entities.Tree)
        return True
    return False

def plantTrees(plant_amount=10):
    moveTo(0, 0)
    
    for i in range(plant_amount):
        while True:
            current_x, current_y = get_pos_x(), get_pos_y()
            ground = get_ground_type()
            
            if can_harvest():
                harvest()
            
            if ground == Grounds.Soil:
                if get_water() < 0.75:
                    use_item(Items.Water_Tank)
            
            if not should_plant_tree(current_x, current_y, ground) and ground == Grounds.Soil:
                till()
            
            move(North)
            if get_pos_y() == 0:
                move(East)
            
            if [get_pos_x(), get_pos_y()] == [0, 0]:
                break