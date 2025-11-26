# 💰 Procedural Game Economy & Balance Simulator - DESIGN DOCUMENT

This document outlines the core architectural components of the Python simulation, focusing on the **Object-Oriented Programming (OOP) classes** and their relationships.

## 1. Core Classes (UML/Class Structure)

The simulation relies on four primary classes to model the game's economic actors and elements: `Player`, `Resource`, `Market`, and `GameSession`.

### Class: Player (`player.py`)

Models the individual agents (players) interacting with the economy.

|**Field**|**Type**|**Description**|
|---|---|---|
|`player_id`|`str`|Unique ID for tracking.|
|`currency`|`float`|Player's current gold/in-game currency.|
|`inventory`|`dict`|Stores `Resource` objects and quantities.|
|`progression_level`|`int`|Represents how far the player has advanced.|

|**Method**|**Description**|
|---|---|
|`earn_currency(amount)`|Adds currency to the player (faucet).|
|`spend_currency(cost)`|Reduces currency (sink); checks for affordability.|
|`craft_item(item_recipe)`|Consumes resources and currency to create a new item.|
|`log_activity()`|Records economic actions to the main simulation log.|

### Class: Resource (`resource.py`)

Models items, materials, and currency used in the economy.

|**Field**|**Type**|**Description**|
|---|---|---|
|`name`|`str`|Unique name (e.g., 'Copper Ore', 'Health Potion').|
|`rarity`|`str`|Defines drop rate probability ('Common', 'Rare', 'Legendary').|
|`base_cost`|`float`|Theoretical value used by the market.|
|`is_craftable`|`bool`|Can this item be manufactured by a player?|

### Class: Market (`market.py`)

Models the central point of economic exchange and manages prices.

|**Field**|**Type**|**Description**|
|---|---|---|
|`price_history`|`dict`|Tracks the average selling price over time.|
|`supply`|`dict`|Tracks the total available quantity of each resource.|
|`demand`|`dict`|Tracks how many resources players attempt to buy.|

|**Method**|**Description**|
|---|---|
|`calculate_price(resource_name)`|Dynamically adjusts price based on supply/demand ratio.|
|`execute_trade(player, resource, quantity)`|Handles the transaction between the player and the central market.|

### Class: GameSession (`simulation.py`)

The main logic runner. Initializes the world, runs the simulation loop, and logs data.

|**Method**|**Description**|
|---|---|
|`initialize_world(num_players, initial_resources)`|Creates all initial `Player` objects and sets starting conditions.|
|`run_cycle(time_steps)`|Executes the main loop, calling `Player` methods (earn, spend, craft) randomly to simulate activity.|
|`analyze_log()`|Processes the raw data log to generate key metrics (e.g., average currency inflation, resource distribution).|

## 2. Simulation Workflow

1. **Initialization:** `GameSession` is created. All `Player` and `Resource` objects are instantiated.
    
2. **Loop:** The `GameSession` runs for a fixed number of `time_steps`.
    
3. **Action:** In each step, a random `Player` performs a random economic action (e.g., mining a resource, buying a potion, crafting an item).
    
4. **Logging:** Every action and its economic impact (price change, currency change) is logged via `Player.log_activity()`.
    
5. **Analysis:** After the loop, `GameSession.analyze_log()` uses **Pandas** to turn the log data into balance reports.
