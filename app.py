import streamlit as st
from puzzle import PUZZLE, solve_puzzle
from architectures import run_architecture

st.set_page_config(
    page_title="Multi-Agent Puzzle Solver",
    page_icon="🧩",
    layout="wide"
)

st.title("🧩 Multi-Agent Collaborative Puzzle Solver")
st.caption("Distributed Puzzle Solving using Centralized, Hierarchical and Blackboard Architectures")

with st.sidebar:
    st.header("Architecture")
    architecture = st.selectbox(
        "Choose an architecture",
        ["Centralized", "Hierarchical", "Blackboard"]
    )

    st.markdown("---")
    st.subheader("Puzzle")
    st.write("🏝️ Lost Treasure Island Puzzle")

st.markdown("## 🏝️ Lost Treasure Island Puzzle")

st.info(
    "Five explorers visited five different islands. Each explorer had a "
    "different boat and discovered a different treasure. Use the clues "
    "to determine who discovered the Golden Crown."
)

with st.expander("View puzzle clues"):
    for i, clue in enumerate(PUZZLE["clues"], 1):
        st.write(f"**{i}.** {clue}")

if st.button("🚀 Solve Puzzle", type="primary", use_container_width=True):
    with st.spinner("Agents are collaborating..."):
        solution = solve_puzzle()

    st.markdown(f"### Architecture: `{architecture}`")
    st.markdown("### 🤖 Agent Collaboration")

    logs = run_architecture(architecture, solution)

    for log in logs:
        st.write(log)

    st.divider()
    st.success(
        f"🏆 **Final Answer:** {solution['explorer']} discovered "
        f"the **{solution['treasure']}** on **{solution['island']}** "
        f"using the **{solution['boat']}**."
    )

    st.markdown("### 📊 Solved Configuration")

    cols = st.columns(5)
    for i, item in enumerate(solution["table"]):
        with cols[i]:
            st.metric(f"Position {i+1}", item["island"])
            st.write(f"👤 {item['explorer']}")
            st.write(f"🚤 {item['boat']}")
            st.write(f"💎 {item['treasure']}")

st.markdown("---")
st.caption("Multi-Agent Systems Mini Project | Distributed Puzzle Solving")
