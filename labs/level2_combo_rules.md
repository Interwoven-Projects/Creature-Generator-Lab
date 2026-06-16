# Level 2 Lab Challenge: Region + Stat Combo Rules

**Creature Generator Educational Lab**  
**Goal:** Make certain region + stat combinations produce special, thematic avatars that feel unique to that environment.

---

## Learning Objectives

By completing this challenge you will:

- Write conditional logic that checks **both** the region and one or more stats
- Create "special case" rules that make some creatures feel rare or flavorful
- Practice thinking about game balance and fantasy theming
- Build on top of Level 1 (Secondary Stat Boost)

---

## Why This Challenge Matters

Level 1 made avatars show two stats when they are close in power.  
Level 2 goes further: it lets you create **special rules** that only apply in certain regions.

Examples of the kind of flavor we want:
- A highly creative creature born in the **Volcano** should feel different from a creative creature born in the **Forest**.
- An intelligent creature from the **Ocean** might feel like a "wise current" or deep-sea sage.
- A strong + fast creature from the **Plains** could be a "wild runner" or guardian of the grasslands.

These special combos make the world feel more alive and give students a taste of designing game mechanics.

---

## The Challenge

**File to edit:** `creature.py` → `_choose_avatar()` function

### Starting Point
You should have Level 1 (secondary stat boost) working first.  
Then you will add new `if` / `elif` rules that check the `region` **and** specific stat values.

### Your Mission
Add at least **3–5 special combo rules** that change or enhance the avatar when certain conditions are met.

You can make the rules as simple or as creative as you like.

---

## Suggested Combo Ideas (Feel Free to Invent Your Own)

| Region     | Condition                          | Suggested Avatar Change          | Flavor Idea              |
|------------|------------------------------------|----------------------------------|--------------------------|
| Volcano    | High creativity                    | Add `🔥🎨` or change to `🌋🧊`     | Magma Forger / Artist    |
| Ocean      | High intelligence                  | Add `🧠` or `🌊🧠`                 | Deep Current Sage        |
| Forest     | High strength + high speed         | Add `🛡️⚡`                         | Wild Guardian            |
| City       | High charm + high intelligence     | Add `✨🧠`                         | Charismatic Innovator    |
| Mountain   | Very high strength                 | Add `⛰️💪` or make it `🏔️🪨`       | Peak Defender            |
| Desert     | High speed                         | Add `🏜️⚡`                         | Dune Racer               |
| Tundra     | High intelligence                  | Add `❄️🧠`                         | Frost Thinker            |
| Plains     | High speed + high charm            | Add `🌾⚡✨`                        | Grassland Herald         |

You don’t have to use all of these — pick the ones that excite you and invent 1–2 of your own.

---

## Step-by-Step Instructions

1. Make sure **Level 1** is complete and tested.
2. Open `creature.py` and go to the `_choose_avatar` function.
3. After your Level 1 code (but before the final `return`), add new conditional blocks.
4. Use `if`, `elif`, and comparisons like `stats.get("creativity", 0) > 80`.
5. Test frequently using the terminal command from Level 1.
6. When you’re happy with your rules, show off a few of your favorite creatures!

---

## Example Code Pattern

```python
# After your Level 1 code...

# Level 2: Special Region + Stat Combos
if region == "Volcano" and stats.get("creativity", 0) > 80:
    avatar = "🌋🔥🎨"          # Magma Forger

elif region == "Ocean" and stats.get("intelligence", 0) > 85:
    avatar += "🧠"             # Wise current / Deep sage

elif region == "Forest" and stats.get("strength", 0) > 90 and stats.get("speed", 0) > 80:
    avatar = "🌲🛡️⚡"          # Wild Guardian

# Add more of your own rules below...
```

You can also make some rules **add** to the existing avatar instead of replacing it.

---

## Success Criteria

You have completed Level 2 when:

- You have added at least 3 meaningful combo rules.
- The rules only trigger in specific regions with specific stats.
- Creatures feel more unique and thematic.
- Your code is still readable (use comments to explain unusual rules).
- You can generate several creatures and see your special avatars appear.

---

## Reflection Questions

- Which combo rule was your favorite to create and why?
- Did any of your rules accidentally override Level 1 behavior? How did you fix it?
- How would you make these rules easier for someone else to edit later without changing the Python code? (This question points toward Level 3!)

---

## What’s Next?

After finishing Level 2, the next challenge (Level 3) will combine:
- Using the SQT birth seed/tick to create **rarity tiers** (common / rare / legendary)
- Moving many of the rules into an external `avatar_rules.json` file

This will be a bigger step, but very powerful.

---

**Remember:** The goal is not just to make cool emojis — it’s to practice writing clear logic that expresses creative ideas. Have fun designing your creature world!

*Part of the Creature Generator Educational Lab – June 2026*
