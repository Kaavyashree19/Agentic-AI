# 🧩 Multi-Agent Collaborative Distributed Puzzle Solver

A mini-project demonstrating how multiple software agents can collaborate to solve a distributed logic puzzle using three architectures:

1. Centralized Architecture
2. Hierarchical Architecture
3. Blackboard Architecture

## Puzzle

The project uses an original Lost Treasure Island puzzle.

Five explorers visit five islands using different boats and finding different treasures. Agents analyze the constraints and determine who discovered the Golden Crown.

## Architecture

### Centralized
A Master Agent controls task allocation, receives worker results and produces the final answer.

### Hierarchical
A Main Coordinator manages specialized sub-coordinators, which manage individual worker agents.

### Blackboard
Agents communicate indirectly through a shared Blackboard containing the current knowledge and intermediate results.

## Run the Web App

Install Python 3.9+.

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

The browser will open the web interface.

## Run Individual Versions

```bash
python centralized/centralized_solver.py
python hierarchical/hierarchical_solver.py
python blackboard/blackboard_solver.py
```

## Final Answer

The puzzle solution is:

**Kavin discovered the Golden Crown on the Golden Island using the Wave boat.**

## Project Structure

```text
distributed-puzzle-solver/
├── app.py
├── puzzle.py
├── architectures.py
├── requirements.txt
├── README.md
├── centralized/
│   └── centralized_solver.py
├── hierarchical/
│   └── hierarchical_solver.py
└── blackboard/
    └── blackboard_solver.py
```
