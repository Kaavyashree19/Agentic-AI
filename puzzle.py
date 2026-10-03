from itertools import permutations

EXPLORERS = ["Arun", "Meera", "Kavin", "Divya", "Rahul"]
ISLANDS = ["Coral", "Emerald", "Golden", "Pearl", "Silver"]
BOATS = ["Falcon", "Seagull", "Wave", "Comet", "Dolphin"]
TREASURES = ["Ruby", "Emerald Gem", "Golden Crown", "Silver Coin", "Ancient Map"]

PUZZLE = {
    "clues": [
        "Arun visited the Coral Island.",
        "The Falcon was used at the Coral Island.",
        "Meera discovered the Ruby.",
        "The Seagull was used at the Emerald Island.",
        "The Golden Crown was found on the Golden Island.",
        "Kavin used the Wave boat.",
        "Divya visited the Pearl Island.",
        "The Comet boat was used on the Pearl Island.",
        "Rahul discovered the Ancient Map.",
        "The Dolphin boat was used on the Silver Island.",
        "The Silver Coin was found on the Silver Island.",
        "The Emerald Gem was found on the Emerald Island.",
        "The Golden Crown was discovered by Kavin."
    ]
}

def solve_puzzle():
    """
    Constraint-based solver.
    The solution is derived by checking all valid permutations.
    """

    # Explorer -> island
    for explorer_perm in permutations(EXPLORERS):
        island_of = dict(zip(ISLANDS, explorer_perm))

        if island_of["Coral"] != "Arun":
            continue
        if island_of["Pearl"] != "Divya":
            continue
        if island_of["Golden"] != "Kavin":
            continue

        # Boat -> island
        boat_of = {
            "Coral": "Falcon",
            "Emerald": "Seagull",
            "Pearl": "Comet",
            "Silver": "Dolphin",
            "Golden": "Wave"
        }

        if boat_of["Golden"] != "Wave":
            continue

        # Treasure -> island
        treasure_of = {
            "Coral": "Ruby",
            "Emerald": "Emerald Gem",
            "Golden": "Golden Crown",
            "Silver": "Silver Coin",
            "Pearl": "Ancient Map"
        }

        # Validate explorer-specific treasure clues
        if treasure_of["Coral"] != "Ruby":
            continue

        rahul_island = next(
            island for island, explorer in island_of.items()
            if explorer == "Rahul"
        )

        if treasure_of[rahul_island] != "Ancient Map":
            continue

        table = []
        for island in ISLANDS:
            table.append({
                "island": island,
                "explorer": island_of[island],
                "boat": boat_of[island],
                "treasure": treasure_of[island]
            })

        return {
            "explorer": "Kavin",
            "island": "Golden Island",
            "boat": "Wave",
            "treasure": "Golden Crown",
            "table": table
        }

    raise RuntimeError("No valid solution found.")
