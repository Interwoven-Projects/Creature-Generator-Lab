# Creature Generator — Educational Lab

**A beginner-friendly project for motivated teens learning to code**

This lab is part of the broader **Interwoven Projects** educational efforts — an open community focused on interdisciplinary learning, contribution, and accreditation across coding, systems, philosophy, and creative projects.

Build a fun Streamlit web app that generates unique creatures based on birth region, stats, and a Squirrel-Quantum-Time (SQT) inspired seed. Then extend it through four progressive challenges.

---

## Project Goals

This lab is designed to teach real software development concepts while keeping things fun and visual:

- Separate **logic** from **user interface** (good code organization)
- Use **external data** (JSON) so non-coders can tweak the experience
- Understand **procedural generation** with seeds (reproducibility)
- Practice **creative problem-solving** through avatar rules and rarity systems
- Experience the power of **data-driven design**

By the end, you will have built something you can show off — and you’ll understand *why* the code is structured the way it is.

---

## What You’ll Build

A web app where you can:
- Enter a creature name and choose a birth region (Forest, Volcano, Ocean, etc.)
- Generate a creature with stats influenced by its region
- See a beautiful **radar chart** of its abilities
- Get a unique **emoji avatar** that reflects its strengths
- Download the creature as a JSON file
- Extend the system through four fun coding challenges

---

## Project Structure

```
coding_intro/
├── app.py                 # Streamlit user interface (presentation layer)
├── creature.py            # All the logic: generation, SQT seeding, avatars
├── regions.json           # Data file — easy to edit regions and modifiers
├── avatar_rules.json      # (Level 4) Rules for combos and rarity
├── requirements.txt
├── README.md              # You are here
└── labs/                  # Individual challenge guides
    ├── level1_avatar_challenge.md
    ├── level2_combo_rules.md
    ├── level3_rarity_sqt.md
    └── level4_data_driven_rules.md
```

**Key Principle:** `app.py` only handles the website. All the important logic lives in `creature.py`. This makes the code much easier to understand and test.

---

## Getting Started

### 1. Setup

```bash
# Clone or download this repository
cd coding_intro

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate          # Mac/Linux
# .venv\Scripts/activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

Open the link that appears in your browser. Try generating a few creatures!

---

## Learning Path (4 Challenges)

Work through these challenges in order. Each one builds on the previous.

| Level | Challenge                        | Focus                              | Difficulty | Link |
|-------|----------------------------------|------------------------------------|------------|------|
| **1** | Secondary Stat Boost             | Use `sorted()` to show top 2 stats | Easy       | [Level 1](labs/level1_avatar_challenge.md) |
| **2** | Region + Stat Combo Rules        | Add special rules for region + stats | Medium   | [Level 2](labs/level2_combo_rules.md) |
| **3** | Rarity & SQT Influence           | Use the birth seed for rarity tiers + optional SQT exploration | Medium+ | [Level 3](labs/level3_rarity_sqt.md) |
| **4** | Data-Driven Avatar Rules         | Move rules into `avatar_rules.json` (advanced) | Hard | [Level 4](labs/level4_data_driven_rules.md) |

**Tip:** Complete the code changes for each level, then test by running `streamlit run app.py` or using the terminal test commands in the lab pages.

---

## How the Creature System Works

1. You choose a **name** and **region**.
2. The app calls `generate_creature()` in `creature.py`.
3. A **seed** is created by mixing:
   - A hash of the creature’s name
   - An SQT-inspired time value (`get_sqt_inspired_seed()`)
   - The region
4. Stats are generated and modified by the region’s multipliers in `regions.json`.
5. An **avatar** is built using rules you will improve in the challenges.
6. The result is displayed with a radar chart and can be downloaded as JSON.

---

## Extending the Project

Once you finish the four challenges, here are some ideas for going further:

- Add new regions to `regions.json`
- Create more creative avatar rules in Level 2 or 4
- Add a “My Creatures” gallery using `st.session_state`
- Let users upload their own `avatar_rules.json`
- Connect more deeply with Squirrel-Quantum-Time concepts (see Level 3 stretch goals)

The project is designed to be easy to modify. Have fun making it yours!

---

## How to Share Your Work

After finishing the challenges, here are some ways to share what you created:

### Quick & Simple Options
- Take screenshots of your favorite creatures (especially Legendary ones!) and share them with friends or your class.
- Fork this repository on GitHub and submit a **Pull Request** with your changes.

### Planned for the Future Educational Hub
A more structured submission method is planned for the central Interwoven Projects educational hub:

- **Export your creature as JSON** (using the Download button) + write a short reflection about what you learned or created.
- This will make it easier to review, share, and accredit completed labs across multiple educational resources.

For now, feel free to use the simple methods above. The JSON + Reflection approach will become available as the hub develops.

---

## For Teachers & Facilitators

This lab works well with motivated teenagers (roughly ages 13–17) who have some comfort with basic Python (variables, functions, conditionals). No prior web development experience is needed.

### Suggested Pacing
- **Level 1**: 30–60 minutes (quick win, builds confidence)
- **Level 2**: 45–75 minutes
- **Level 3**: 45–90 minutes (including optional SQT exploration)
- **Level 4**: 60–120+ minutes (most advanced — best for students who enjoy abstraction)

Students can work individually or in pairs. Many enjoy sharing their favorite creatures and creative rules with the group.

### Teaching Tips
- Encourage students to **test frequently** using the terminal commands provided in each lab page.
- When students get stuck, ask guiding questions rather than giving the answer directly (e.g., “What happens if you print the sorted stats?”).
- Celebrate creativity — there are many valid ways to solve each challenge.
- Level 4 is significantly harder than the others. It’s okay if not every student reaches it in one session.
- The optional SQT exploration in Level 3 is great for students who are curious about the time system or want to connect it to the original Squirrel-Quantum-Time project.

### Classroom / Group Ideas
- Have students present one creature they’re proud of and explain the rule they added.
- Create a shared “bestiary” by collecting everyone’s favorite creatures.
- Use the radar chart as a discussion point: “Which stat combination feels most powerful to you and why?”

### Prerequisites
- Basic Python (variables, functions, `if` statements, dictionaries)
- Comfort running commands in a terminal
- A modern web browser (for Streamlit)

No advanced math or prior experience with Streamlit or Plotly is required — students learn what they need as they go.

---

## Credits & Inspiration

- Built as an educational lab for learning Python, Streamlit, and good software design
- SQT (Squirrel-Quantum-Time) concept by Squirrel814
- Created with ❤️ and a lot of acorn energy

---

**Ready to begin?** Start by running the app, then open **Level 1** and follow the instructions!

Happy creature forging! 🧬✨
