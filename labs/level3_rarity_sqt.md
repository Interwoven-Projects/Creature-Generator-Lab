# Level 3 Lab Challenge: Rarity & SQT Influence

**Creature Generator Educational Lab**  
**Goal:** Use the SQT-inspired birth seed to give creatures rarity tiers (Common / Rare / Legendary) and special visual effects.

---

## Learning Objectives

By the end of this challenge you will be able to:

- Use the modulo operator (`%`) with the creature’s `seed_used` or `sqt_tick_at_birth` to create rarity
- Add conditional visual flair based on rarity
- Connect the Unique Time Calculator (SQT) concept to meaningful gameplay/visual outcomes
- Think about probability and “specialness” in procedural generation

---

## Why This Challenge Matters

Up until now, every creature has been equally likely to appear.  
In many games and simulations, some creatures feel more special because they are **rare**.

By using the birth seed (which already comes from our SQT-inspired time system), we can make certain creatures feel legendary without needing true randomness. This is a very common technique in game development called **seeded procedural generation**.

This challenge also reinforces why we built the SQT time system in the first place — it’s not just decoration; it can drive interesting mechanics.

---

## The Challenge

**File to edit:** `creature.py` → `_choose_avatar()` (and possibly `generate_creature()`)

### Your Mission

1. Determine a rarity tier for the creature using its `seed_used` or `sqt_tick_at_birth`.
2. Modify the avatar to show special visual effects based on rarity.
3. (Optional but recommended) Add a `"rarity"` key to the creature dictionary so it can be displayed in the app later.

### Suggested Rarity Tiers

| Rarity     | Condition              | Visual Effect             | Example Avatar      |
|------------|------------------------|---------------------------|---------------------|
| **Legendary** | `seed % 100 < 5`      | Add `👑` or `✨✨`         | `🌋👑💪`             |
| **Rare**      | `seed % 100 < 20`     | Add `✨`                   | `🌲✨🎨`             |
| **Common**    | Everything else       | No extra symbols          | `🌊⚡`               |

You can adjust the percentages (5% legendary, 15% rare, 80% common is a classic distribution).

---

## Step-by-Step Instructions

1. Complete **Level 2** first (combo rules).
2. In `_choose_avatar()`, after your Level 2 code, add logic that checks the `seed` parameter.
   - Note: Currently `_choose_avatar` only receives `region` and `stats`. You may need to also pass the `seed` into this function (or calculate rarity in `generate_creature` and pass a `rarity` string instead).
3. Update the avatar string based on the rarity tier.
4. (Bonus) Modify `generate_creature()` to include a `"rarity"` field in the returned dictionary.
5. Test by generating many creatures and looking for the special ones.

---

## Important Hint About the Function Signature

Right now `_choose_avatar(region, stats)` does not receive the seed.  

You have two good options:

**Option A (Simpler for Level 3):**  
Calculate rarity inside `generate_creature()` and pass a `rarity` string to `_choose_avatar()`.

**Option B (More advanced):**  
Change the function signature to `_choose_avatar(region, stats, seed)` and update the call site in `generate_creature()`.

Both are valid. Option A is slightly easier for this level.

---

## Example Code Sketch

```python
# Inside generate_creature(), after creating stats:
seed = ...   # the seed you already calculated

# Determine rarity
if seed % 100 < 5:
    rarity = "Legendary"
elif seed % 100 < 20:
    rarity = "Rare"
else:
    rarity = "Common"

# Then pass it to the avatar function (you will need to update the call)
avatar = _choose_avatar(region, final_stats, seed, rarity)
```

Then in `_choose_avatar`:

```python
def _choose_avatar(region, stats, seed=None, rarity="Common"):
    ...
    if rarity == "Legendary":
        avatar += "👑"
    elif rarity == "Rare":
        avatar += "✨"
```

---

## Success Criteria

You have completed Level 3 when:

- Creatures have a visible rarity system driven by their SQT birth seed.
- Legendary and Rare creatures appear noticeably less often than Common ones.
- The avatar clearly communicates rarity (through extra symbols or changed emojis).
- You can explain how the modulo operation creates rarity from a deterministic seed.

---

## Reflection Questions

- Why is it useful that rarity is based on the seed instead of pure random chance?
- What happens to rarity if someone uses a custom seed? Is that good or bad?
- How could you let players influence rarity in a future version of the app?

---

## What’s Next?

**Level 4** will be the most advanced challenge: moving many of the avatar rules (including rarity thresholds and combo rules) into an external `avatar_rules.json` file. This is a big step toward professional-grade, data-driven design.

---

## Going Deeper with SQT (Optional Exploration)

If you're especially interested in the **Squirrel-Quantum-Time** system, here are some optional ways to experiment further:

### 1. Custom "Quantum Day" Length
The real SQT uses a ~37.3-hour "quantum day" instead of 24 hours. 

You can explore this idea by:
- Adding a constant near the top of `creature.py`:
  ```python
  SQT_DAY_HOURS = 37.301826   # Real SQT quantum day length
  ```
- Modifying `get_sqt_inspired_seed()` to use this value when calculating the tick (for example, by scaling the time components).
- Observe how changing this value affects how quickly rarity changes between creature generations.

### 2. Connect Rarity to "Lunation" Ideas
In full SQT, there are 19-day lunations with themed moon names. You could experiment with:
- Using `seed % 19` to create different "lunation phases"
- Giving creatures born in certain phases a small bonus or special visual (e.g., "Pinecone Moon" creatures get a `🌲` bonus emoji)

These are **stretch goals** — not required for completing Level 3, but great ways to connect more deeply with the SQT concept behind the Unique Time Calculator.

---

**Remember:** Rarity systems are one of the most satisfying parts of procedural generation. Enjoy hunting for your first Legendary creature!

*Part of the Creature Generator Educational Lab – June 2026*
