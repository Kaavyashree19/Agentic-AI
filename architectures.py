def run_architecture(architecture, solution):
    """Generate transparent collaboration logs for each architecture."""

    if architecture == "Centralized":
        return [
            "🧠 Master Agent: Received the complete puzzle.",
            "📋 Master Agent: Dividing the puzzle into island, boat and treasure tasks.",
            "👤 Explorer Agent: Checking explorer–island relationships.",
            "🚤 Boat Agent: Checking boat–island relationships.",
            "💎 Treasure Agent: Checking treasure–island relationships.",
            "🔎 Master Agent: Collecting and validating worker results.",
            "✅ Master Agent: All constraints are consistent.",
            "🏆 Master Agent: Final solution generated."
        ]

    if architecture == "Hierarchical":
        return [
            "🧠 Main Coordinator: Received the puzzle.",
            "🏝️ Island Coordinator: Delegating location constraints.",
            "   ├── Island Agent: Checking explorer locations.",
            "   └── Position Agent: Validating island relationships.",
            "🎒 Resource Coordinator: Delegating boat and treasure constraints.",
            "   ├── Boat Agent: Checking boat assignments.",
            "   └── Treasure Agent: Checking treasure assignments.",
            "🔄 Coordinators: Reporting validated results to Main Coordinator.",
            "🏆 Main Coordinator: Combining results and generating solution."
        ]

    if architecture == "Blackboard":
        return [
            "🗃️ Blackboard: Puzzle and initial constraints posted.",
            "👤 Explorer Agent: Reading constraints from Blackboard.",
            "✍️ Explorer Agent: Posting explorer–island findings.",
            "🚤 Boat Agent: Reading updated Blackboard knowledge.",
            "✍️ Boat Agent: Posting boat–island findings.",
            "💎 Treasure Agent: Reading all current knowledge.",
            "✍️ Treasure Agent: Posting treasure–island findings.",
            "🔎 Logic Agent: Detecting consistency across all posted facts.",
            "🔄 Blackboard: Knowledge converged to a consistent solution.",
            "🏆 Coordinator: Reading the final Blackboard state."
        ]

    return []
