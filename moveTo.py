def moveTo(pos_x, pos_y):
    world_size = get_world_size()
    
    current_x, current_y = get_pos_x(), get_pos_y()
    
    x_diff = current_x - pos_x
    wrap_left_distance = current_x + world_size - pos_x
    wrap_right_distance = world_size - current_x + pos_x
    
    y_diff = pos_y - current_y
    wrap_up_distance = world_size - current_y + pos_y
    wrap_down_distance = current_y + world_size - pos_y
    
    amount_x = wrap_left_distance
    x_direction = West
    if current_x != pos_x:
        if abs(x_diff) < min(wrap_left_distance, wrap_right_distance):
            amount_x = abs(x_diff)
            x_direction = West
            if x_diff < 0:
                x_direction = East
        elif wrap_left_distance > wrap_right_distance:
            amount_x = wrap_right_distance
            x_direction = East
    else:
        amount_x = 0
    
    amount_y = wrap_up_distance
    y_direction = North
    if current_y != pos_y:
        if abs(y_diff) < min(wrap_up_distance, wrap_down_distance):
            amount_y = abs(y_diff)
            y_direction = North
            if y_diff < 0:
                y_direction = South
        elif wrap_up_distance > wrap_down_distance:
            amount_y = wrap_down_distance
            y_direction = South
    else:
        amount_y = 0
    
    for i in range(amount_x):
        move(x_direction)
    for i in range(amount_y):
        move(y_direction)
        