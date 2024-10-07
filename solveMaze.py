def solveMaze():
	directions = [North, East, South, West]
	directionIndex = 0
	while get_entity_type() != Entities.Treasure:
		if move(directions[directionIndex]):			
			directionIndex += 1
			if directionIndex >= 4:
				directionIndex = 0
		else:
			directionIndex -= 1
			if directionIndex < 0:
				directionIndex = 3
	harvest()