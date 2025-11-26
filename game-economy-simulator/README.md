# 💰 Procedural Game Economy & Balance Simulator

## Project Summary

This project is a sophisticated **Object-Oriented Programming (OOP) simulation** designed to model and stress-test the complex systems within a video game economy. It runs millions of simulated player actions to log resource generation, currency flow, and item consumption.

The primary goal is to identify and prevent **economic exploits (like inflation or hyper-deflation)** and ensure long-term stability and fairness in procedurally generated game worlds. This project showcases strong system design and OOP modeling skills, vital for building scalable Generative AI systems.

## Technical Highlights

|Feature|Description|Relevant Skill / Technology|
|---|---|---|
|**System Modeling**|Defines and manages complex interactions between `Player`, `Market`, and `Resource` objects.|Python **Object-Oriented Programming (OOP)**, System Design|
|**Stress Testing**|Employs **Monte Carlo simulation** techniques to run millions of virtual player hours, generating massive, repeatable datasets.|Statistical Modeling, Advanced Python Scripting|
|**Balance Analysis**|Uses data wrangling to analyze simulation output for non-linear growth patterns that indicate potential exploits.|**Pandas** for Data Analysis, Statistical Reporting|
|**Design Documentation**|The full class structure and methodology are documented in `docs/DESIGN.md`.|Software Documentation, Modular Design|

## Repository Structure

The project follows a clean, modular structure for logic and data separation:

```
game-economy-simulator/
├── docs/                 # Design documents, including the Class Structure (DESIGN.md)
├── src/                  # Core Python source code
│   ├── core/             # Modular classes (player.py, resource.py, simulation.py)
│   └── main.py           # Entry point for running the simulation
├── data/                 # Folder to store simulation logs
└── requirements.txt      # Lists necessary packages
```

## Setup and Installation

### Requirements

This project requires **Python 3.8+** and the following packages, detailed in `requirements.txt`:

- `pandas`
    
- `numpy`
    
- `matplotlib` (for graphing stability over time)
    

### How to Run

1. **Clone the Repository:**
    
    ```
    git clone [https://github.com/ryangilbert-github/Phase1-Foundational-Data-Systems/game-economy-simulator.git](https://github.com/ryangilbert-github/Phase1-Foundational-Data-Systems/game-economy-simulator.git)
    cd Phase1-Foundational-Data-Systems/game-economy-simulator
    ```
    
2. **Install Dependencies:**
    
    ```
    pip install -r requirements.txt
    ```
    
3. **Run the Simulation (WIP):** _[Instructions for running the simulation will be added here upon completion of the relevant **Python OOP and Data Science** modules in the 100 Days of Code Bootcamp.]_
    

## Status: Work in Progress 🛠️

This project is actively being developed. The **Object-Oriented Design** is complete, and the coding phase will commence upon mastery of the relevant Python modules in the current learning roadmap.
