def plantBush(plant_amount=10):
    for i in range(plant_amount):
        moveTo(0, 0)
        do_a_flip()
        while True:
            if get_entity_type() == Entities.Hedge:
                solveMaze()
                break

            if get_ground_type() == Grounds.soil:
                till()
            
            if can_harvest():
                if get_entity_type() != Entities.Bush:
                    harvest()
                    plant(Entities.Bush)
                trade(Items.Fertilizer)
                use_item(Items.Fertilizer)
            
            move(North)
            if get_pos_y() == 0:
                move(East)
                if get_pos_x() == 4:
                    moveTo(0, 0)