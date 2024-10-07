def callPlanting(wants):
    items_map = {
        Items.Hay: (Items.Hay, plantTrees),
        Items.Wood: (Items.Wood, plantTrees),
        Items.Gold: (Items.Gold, plantBush),
        Items.Carrot: (Items.Carrot_seed, plantCarrot),
        Items.Pumpkin: (Items.Pumpkin_seed, plantPumpkin),
        Items.Power: (Items.Sunflower_Seed, plantSunflower),
        Items.Cactus: (Items.Cactus_Seed, plantCactus)
    }

    world_size = get_world_size()
    plant_area = world_size * world_size

    for item_wanted in wants:
        amount_wanted = wants[item_wanted] * 1000
        while num_items(item_wanted) < amount_wanted:
            requirements = get_cost(items_map[item_wanted][0])
            for item_needed in requirements:
                amount_needed = requirements[item_needed] * plant_area
                while num_items(item_needed) < amount_needed:
                    items_map[item_needed][1]()
            items_map[item_wanted][1]()

    print("All requirements met, auto planting activated!")

    while True:
        for plant_func in [plantTrees, plantBush, plantCarrot, plantPumpkin, plantSunflower, plantCactus]:
            plant_func()
