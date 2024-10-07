def sortCactus(world_size, direction):
    directional_map = {
        East: (West, get_pos_x),
        North: (South, get_pos_y)
    }
    while True:
        current_measure = measure()
        next_measure = measure(direction)
        if current_measure > next_measure:
            swap(direction)
            old_place = get_pos_x(), get_pos_y()
            
            new_direction, get_pos = directional_map[direction]
            while (get_pos() != 0) and measure() < measure(new_direction):
                swap(new_direction)
                move(new_direction)
            moveTo(old_place[0], old_place[1])

        if direction == East and get_pos_x() != world_size - 1:
            move(direction)
        elif direction == North and get_pos_y() != world_size - 1:
            move(direction)
        else:
            move(direction)
            if direction == East:
                move(North)
            else:
                move(East)
            return

def plantCactus(amount_to_harvest=1):
    world_size = get_world_size()
    planting_area = world_size * world_size
    
    amount_planted, harvested_amount = 0, 0
    while harvested_amount < amount_to_harvest:
        if get_ground_type() != Grounds.Soil:
            till()
        if get_entity_type() != Entities.Cactus:
            harvest()
            trade(Items.Cactus_Seed)
            plant(Entities.Cactus)
        
        if amount_planted >= planting_area:
            moveTo(0, 0)
            direction = North
            for i in range(2):
                for layers in range(world_size):
                    sortCactus(world_size, direction)
                direction = East
            harvest()
            amount_planted = 0
            harvested_amount += 1
        
        amount_planted += 1
        move(North)
        if get_pos_y() == 0:
            move(East)
            