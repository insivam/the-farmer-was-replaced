## Introduction
This project showcases my Python programming skills within the context of the game 'The Farmer Was Replaced'. Whether you're just exploring my portfolio or a fellow player, this README will guide you through my automation solutions.

### Game Overview: *The Farmer Was Replaced*

*The Farmer Was Replaced* is a simulation game that challenges players to program a drone using a Python-like language to automate farming tasks. Players optimize the drone's code to efficiently handle resource collection, planting, and harvesting tasks. The game is centered on developing algorithms that improve farming speed and efficiency, allowing players to focus on more complex programming challenges as they progress.

The purpose of your code is to create a fully automated farming system using functions tailored to the different crops and game requirements. The system takes into account plant growth conditions, farm layout, and maze-solving algorithms to ensure the most effective use of resources and time.

# Automation Scripts

## Installation

### Option 1: Using Git (Recommended for Developers)

1. Clone the repository directly into the save folder:

   ```bash
   git clone https://github.com/insivam/the-farmer-was-replaced.git "%UserProfile%\AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced\Saves\"
   ```

2. Restart the game and load the new save "TFWR" which will have the all the code files!

### Option 2: Downloading as a ZIP file

1. Download the repository as a ZIP file from [`here`](https://github.com/insivam/feder-cr/the-farmer-was-replaced/archive/refs/heads/main.zip).

2. Extract the contents of the ZIP file to your game's save folder, which is usually located at:
   
   ```bash
   %UserProfile%\AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced\Saves\
   ```

3. Restart the game and load the new save "TFWR".

## Scripts Breakdown

### [`main.py`](main.py)

The main script that coordinates the planting processes. It defines a dictionary of items and the amount the player wants to collect (e.g., hay, wood, carrots, pumpkins) and uses the callPlanting function.

```python
wants = {
    Items.Hay: 2000,
    Items.Wood: 1500,
    Items.Carrot: 5000,
    Items.Pumpkin: 5000,
    Items.Gold: 50,
    Items.Power: 300,
    Items.Cactus: 150
}
callPlanting(wants)
```

### [`callPlanting.py`](callPlanting.py)

This script manages planting based on the resources the player wants to gather. It maps the items to corresponding planting functions like [`plantTrees`](plantTrees.py), [`plantCarrot`](plantCarrot.py), [`plantCactus`](plantCactus.py), and more.
```python
def callPlanting(wants):
    # Mapping of all scripts needed to run based on the itens
```

### Movement and Pathfinding ([`moveTo.py`](moveTo.py))

While the game provides a default `move()` function, I created a custom movement function that calculates the best path to a target location and calls the in-game `move()` function the correct number of times in the optimal direction. This allows the drone to navigate the farm more efficiently, reducing travel time.

```python
def moveTo(x, y):
    # Pathfinding logic
```

## Planting Scripts

### [`plantCarrot.py`](plantCarrot.py)

Carrots are the simplest crop to plant, but they still require managing soil preparation and water levels. The drone automatically tills the soil if needed and trades for carrot seeds when necessary. Additionally, the drone manages its water supply, ensuring that plants are hydrated. The core challenge here lies in balancing the drone's actions and resources while moving efficiently across the farm.

```python
def plantCarrot(plant_amount=10):
    # Preparation of tilled soil and seed management for efficient carrot planting
```

### [`plantTrees.py`](plantTrees.py)

Tree planting is more complex than carrots because trees require more space and take longer to grow. The script needs to ensure efficient planting cycles while managing the larger plots that trees occupy. Additionally, trees have longer growth periods, requiring careful management of time and resources.

```python
def plantTrees(plant_amount=10):
    # Strategic tree planting with spacing logic to ensure optimal growth rates
```

### [`plantBush.py`](plantBush.py)

Bushes may seem simple at first glance, but they require multiple stages of management. The drone automates the planting of bushes, which can be planted on both grass and soil and provide wood once fully grown. After planting, the drone uses fertilizer to ensure fast growth and to have the chance of teleporting to a maze challenge.

When a teleport occurs, the drone runs the `solveMaze()` script to navigate and complete the maze, then continues with the fertilization and harvesting cycles. This integration of maze-solving logic adds a layer of complexity to the management of bushes, requiring the drone to handle both the maze and farming tasks efficiently.


```python
def plantBush(plant_amount=10):
    # Management of bush planting, fertilization, and maze-solving integration
```

### [`solveMaze.py`](solveMaze.py)
The drone initially starts with no knowledge of the maze, including the locations of walls, its position, or where the treasure is located. To solve this, I implemented a strategy where the drone "hugs" the right wall and follows it continuously. The logic behind this approach ensures that, by always keeping a wall on the right side, the drone will eventually find the treasure. Once the treasure is under the drone, the `solveMaze()` function terminates the search and allows the drone to return to its farming tasks.

```python
def solveMaze():
    # Direction and movement logic for maze solving
```

### [`plantPumpkin.py`](plantPumpkin.py)

Pumpkins grow on tilled soil and require pumpkin seeds, which can be bought using carrots. When fully grown, pumpkins can merge to form a "giant pumpkin," which significantly increases yield. For example, a 2x2 field of pumpkins yields 8 pumpkins instead of 4, and larger fields yield even more. However, about 1 in 5 pumpkins might die before they fully grow, which can prevent the giant pumpkin from forming. The script manages this by monitoring the growth and replanting where necessary.

```python
def plantPumpkin(plant_amount=10):
    # Pumpkin planting and monitoring for growth to form giant pumpkins while managing replanting
```

### [`plantSunflower.py`](plantSunflower.py)

Sunflowers are unique in that they harvest energy from the sun. The power from all sunflowers flows into the sunflower being harvested, which means the drone must harvest the sunflower with the most petals to avoid destroying all the sunflowers. The script uses the measure() function to determine the number of petals and ensures that only the sunflower with the largest petal count is harvested. This optimizes the drone's power usage, as harvesting sunflowers provides energy that can be used to make the drone run faster.

```python
def plantSunflower(plant_amount=10):
    # Sunflower planting with power optimization by harvesting the plant with the most petals
```

### [`plantCactus.py`](plantCactus.py)

The cactus planting task was the most challenging to me due to the requirement for sorting. The cacti must be organized by size, with the smallest cactus at the bottom left and the largest at the top right. To achieve this, my script first plants the cacti, then sorts them by size. The sorting algorithm compares adjacent cacti, and if they are out of order, the drone swaps them.

If two adjacent cacti are of the same size, the drone moves forward to find the correct placement for the next cactus, and then returns to the original position to continue sorting. This process ensures that all cacti are sorted efficiently, allowing them to be harvested for maximum yield. Once sorted, the cacti are ready for harvesting, providing resources only when they are in the correct order.

```python
def plantCactus(plant_amount=10):
    # Sorting and planting of cactus in the correct order for optimal resource harvesting
```

## Unique Features and My Approach to the Challenge

My approach to automating farming in **The Farmer Was Replaced** focused on creating reusable, efficient functions that can handle a variety of tasks, from planting to harvesting and trading. The core challenge in this project was managing the different requirements for each type of plant while optimizing the drone’s movement and resource usage.

### Key Features

1. **Custom Pathfinding**: Although the game provides a default `move()` function, I implemented my own pathfinding function (`moveTo()`). This function calculates the best route for the drone and uses the in-game `move()` function to minimize travel time. By optimizing drone movement, I ensured that the drone could handle larger farms and more complex layouts efficiently.

2. **Resource Management**: Each plant requires different resources (seeds, water, power), and I developed scripts to manage these resources efficiently. The drone automatically trades for seeds, waters crops when necessary, and ensures that it has enough power to continue working.

3. **Automation of Complex Tasks**: While some plants, like carrots and bushes, are relatively simple to automate, others, such as sunflowers and cacti, require more complex logic. For example, cactus planting involves sorting the plants by size, which adds an additional layer of difficulty. I approached these tasks by breaking them down into smaller steps and ensuring that the drone could handle each one systematically.

4. **Efficient Planting Cycles**: For plants like trees and sunflowers that have longer growth periods, I focused on creating scripts that manage planting cycles efficiently. The drone ensures that no time is wasted by managing multiple tasks (e.g., watering, fertilizing) while waiting for plants to grow.

This project demonstrates my ability to take a complex problem and break it down into manageable components. By focusing on optimization and efficiency, I was able to automate farming in a way that scales with the complexity of the game, from simple crops to advanced tasks like cactus sorting and maze solving.

---

## Future Enhancements and Updates
I plan to keep this code updated and compatible with future releases of *The Farmer Was Replaced*. 
As the game evolves, I will optimize the existing functions and ensure compatibility with new game mechanics. 
My goal is to keep improving the automation strategies to achieve greater efficiency and address any new challenges that arise with game updates.

## Contributing

While this project is primarily a personal exploration of game automation, I'm open to feedback and suggestions. Feel free to open an issue if you encounter any problems or have ideas for improvement.

## License
This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.