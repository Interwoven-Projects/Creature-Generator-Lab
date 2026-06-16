"""
app.py — Streamlit presentation layer ONLY.
All creature logic, SQT seeding, and data loading live in creature.py.
This separation teaches students that web UI code should stay thin.

Current state: Educational stub. Shows text output + JSON.
Next milestone: Replace stats display with Plotly radar chart + nice columns.
"""

import streamlit as st
import json
import plotly.graph_objects as go
from creature import generate_creature, load_regions

st.set_page_config(
    page_title="Creature Generator Lab",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 Creature Generator — Educational Lab")
st.caption("Step-by-step rebuild project for motivated teens • SQT-inspired unique time seeding")

# Load regions once
regions = load_regions()
region_names = list(regions.keys())

# --- Sidebar controls ---
with st.sidebar:
    st.header("🧪 Creature Parameters")
    name = st.text_input("Creature Name", value="Acorn", max_chars=30)
    region = st.selectbox("Birth Region", region_names, index=0)
    st.divider()
    use_custom = st.checkbox("Use custom seed (for reproducible results)")
    custom_seed = None
    if use_custom:
        custom_seed = st.number_input(
            "Custom Seed (integer)",
            value=42,
            step=1,
            min_value=0,
            max_value=999999
        )
    st.caption("Leave unchecked for fresh SQT-inspired time seed each generation.")

    generate_clicked = st.button("✨ Generate Creature", type="primary", use_container_width=True)
    if st.button("🔄 New SQT Time (randomize)", use_container_width=True):
        # Force a new generation with fresh time seed by clearing state
        if "creature" in st.session_state:
            del st.session_state.creature
        st.rerun()

# --- Main content ---
st.divider()

if generate_clicked:
    creature = generate_creature(name.strip() or "Unnamed", region, custom_seed)
    st.session_state.creature = creature
elif "creature" in st.session_state:
    creature = st.session_state.creature
else:
    creature = None
    st.info("👉 Fill in the sidebar and click **Generate Creature** to begin your first creation!")

if creature:
    # Header with avatar
    st.subheader(f"{creature['avatar']}  {creature['name']}")
    st.write(f"**Born in:** {creature['region']} — *{creature['region_description']}*")
    st.caption(f"SQT-inspired birth tick: `{creature['seed_used']}` (deterministic • change name/region/seed for new results)")

    # === NEW: Two-column layout with radar chart (Step 2 milestone) ===
    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown("### 📡 Stat Radar")
        # Build radar chart
        categories = list(creature["stats"].keys())
        values = list(creature["stats"].values())
        # Close the loop for polygon
        categories_closed = categories + [categories[0]]
        values_closed = values + [values[0]]

        fig = go.Figure(
            data=[
                go.Scatterpolar(
                    r=values_closed,
                    theta=categories_closed,
                    fill="toself",
                    fillcolor="rgba(100, 200, 255, 0.25)",
                    line=dict(color="#4ECDC4", width=2),
                    name=creature["name"]
                )
            ],
            layout=go.Layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, max(values) + 15],
                        tickfont=dict(size=10)
                    ),
                    angularaxis=dict(tickfont=dict(size=11))
                ),
                showlegend=False,
                margin=dict(l=40, r=40, t=20, b=20),
                height=320
            )
        )
        st.plotly_chart(fig, use_container_width=True, key="radar")

    with col2:
        st.markdown("### 📊 Key Metrics")
        for stat, value in creature["stats"].items():
            # Color hint: higher is "better" for demo (students can change)
            delta_color = "normal"
            st.metric(stat.capitalize(), value, delta_color=delta_color)

        st.markdown("### ✨ Creature Flavor")
        st.success(creature["description"])

    # === NEW: Download button (teaches st.download_button + json.dumps) ===
    st.download_button(
        label="⬇️ Download Creature as JSON",
        data=json.dumps(creature, indent=2, ensure_ascii=False),
        file_name=f"{creature['name'].replace(' ', '_')}_{creature['region']}.json",
        mime="application/json",
        use_container_width=True,
        help="Save this creature to share, version control, or load later in other tools."
    )

    with st.expander("🔍 Full creature data (for learning & debugging)", expanded=False):
        st.json(creature)

    st.divider()
    st.caption("✅ Level 1 Avatar Lab Challenge is now live in creature.py! Open _choose_avatar() and follow the big docstring.")
