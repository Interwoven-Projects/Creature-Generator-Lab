# Level 4 Lab Challenge: Data-Driven Avatar Rules

**Creature Generator Educational Lab**  
**Goal (Advanced):** Move avatar logic, combo rules, and rarity thresholds out of Python code and into an external `avatar_rules.json` file.

---

## Learning Objectives

By completing this challenge you will be able to:

- Load structured data from a JSON file
- Refactor hard-coded logic into data-driven rules
- Understand the benefits of separating **data** from **code**
- Make the creature system much easier for non-programmers to modify

---

## Why This Challenge Matters (The Big Picture)

Up to Level 3, all the rules for avatars, combos, and rarity lived **inside the Python code**.  

This works fine when you are the only person working on the project. But what if:
- A game designer wants to tweak rarity chances?
- An artist wants to add new combo emojis?
- You want to support user-created regions later?

Every time they want to change something, they have to edit Python code (and risk breaking things).

**Level 4** teaches one of the most important ideas in software design:

> **Move configuration and rules into data files whenever possible.**

This is called **data-driven design**, and it is used heavily in professional games, tools, and applications.

---

## The Challenge

**Files you will work with:**
- `creature.py`
- `avatar_rules.json` (new file we provide as a starting point)

### Your Mission

1. Use the provided `load_avatar_rules()` function.
2. Refactor the avatar system so that:
   - Rarity thresholds come from the JSON
   - Combo rules come from the JSON
   - Visual symbols for rarity come from the JSON
3. Make it so that changing `avatar_rules.json` changes creature avatars **without editing any Python code**.

---

## Starter `avatar_rules.json` Structure

We have already created a starter file with this structure:

```json
{
  "rarity_thresholds": {
    "legendary": 5,
    "rare": 20
  },
  "combo_rules": [ ... ],
  "rarity_visuals": {
    "Legendary": "👑",
    "Rare": "✨",
    "Common": ""
  }
}
```

You will need to expand and use this data in your code.

---

## Step-by-Step Guidance

### Step 1: Load the Rules
We have already added `load_avatar_rules()` for you. Call it early in `generate_creature()`.

### Step 2: Calculate Rarity Using JSON Thresholds
Instead of hard-coding `if seed % 100 < 5`, read the thresholds from the loaded rules.

### Step 3: Apply Combo Rules from JSON
Instead of writing many `if region == "Volcano" and ...` statements, loop through the `combo_rules` list from the JSON and apply matching rules.

### Step 4: Use `rarity_visuals` for Final Decoration
After determining rarity, look up the correct symbol in `rarity_visuals` and append it to the avatar.

---

## Example Approach (High Level)

```python
rules = load_avatar_rules()

# 1. Rarity
thresholds = rules["rarity_thresholds"]
if seed % 100 < thresholds["legendary"]:
    rarity = "Legendary"
elif seed % 100 < thresholds["rare"]:
    rarity = "Rare"
else:
    rarity = "Common"

# 2. Apply combo rules (loop through JSON)
for rule in rules["combo_rules"]:
    # check if this rule matches current creature
    ...

# 3. Add rarity visual
visual = rules["rarity_visuals"].get(rarity, "")
avatar += visual
```

---

## Success Criteria

You have completed Level 4 when:

- All major avatar decisions (rarity thresholds, combo rules, visual symbols) are driven by `avatar_rules.json`
- Changing values in the JSON file immediately changes creature generation
- The Python code in `creature.py` is cleaner and more general
- You can explain to someone *why* moving rules to JSON is powerful

---

## Reflection Questions

- What are the advantages of data-driven design?
- What are the disadvantages? (When might hard-coding rules in Python actually be better?)
- How could you extend this system even further (for example, letting users create their own regions with custom rules)?

---

## Congratulations!

If you finish Level 4, you have completed the core avatar extension arc of this lab. You now understand:
- How to process data (`sorted`, comparisons)
- How to add creative domain logic (combos)
- How to use seeds for interesting systems (rarity)
- How to separate data from code (the most professional step)

These are foundational skills that appear in almost every non-trivial program.

---

**You did it.** Great work pushing through all four levels.

*Final challenge in the Creature Generator Educational Lab – June 2026*
