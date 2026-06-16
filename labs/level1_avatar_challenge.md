# Level 1 Lab Challenge: Secondary Stat Boost Avatar

**Creature Generator Educational Lab**  
**Goal:** Make your creature’s emoji avatar tell a richer story by showing both its strongest *and* second-strongest stats when they are close in power.

---

## Learning Objectives

By the end of this challenge you will be able to:

- Use `sorted()` with a `key` function to find the top two values in a dictionary
- Write a clear conditional that compares two numbers
- Combine multiple pieces of information into a single visual result (the avatar string)
- Test your changes quickly from the terminal

---

## Why This Challenge Matters

Right now every creature only shows **one** flavor emoji based on its single highest stat.  
That works, but it hides interesting cases where a creature is *almost* equally good at two things.

For example:
- A Forest creature that is very creative **and** very intelligent should feel different from one that is only creative.
- A Volcano creature that is strong **and** creative could be a “magma artist” instead of just a brute.

Your job is to upgrade the avatar logic so it can show the **region emoji + up to two stat emojis** when the top two stats are competitive.

---

## The Challenge

**File to edit:** `creature.py`  
**Function:** `_choose_avatar(region, stats)`

### Current Behavior (Starting Point)
The function currently returns only the region emoji + one flavor emoji based on the single highest stat.

### Your Mission
Modify the function so that:

1. It still shows the region emoji + dominant stat emoji.
2. **If** the second-highest stat is within **10 points** of the highest stat, it also appends the second flavor emoji.

### Example Outcomes You Should Aim For

| Creature Example              | Possible Avatar     | Why |
|-------------------------------|---------------------|-----|
| Forest, high creativity + high intelligence | `🌲🧠🎨`             | Close second stat |
| Volcano, very high strength only         | `🌋💪`               | Clear dominant stat |
| Ocean, high speed + high charm (within 10) | `🌊⚡✨`             | Competitive stats |

---

## Step-by-Step Instructions

1. Open `creature.py` in your editor.
2. Find the function `_choose_avatar`.
3. Read the big docstring at the top of the function — it contains the full challenge description and a helpful hint.
4. Replace the `# STUDENT CHALLENGE STARTS HERE` section with your own code.
5. Save the file.
6. Test it (see “How to Test” below).

---

## Helpful Hint (from the code)

```python
# You can use this pattern:
sorted_stats = sorted(stats.items(), key=lambda item: item[1], reverse=True)
highest_stat, highest_val = sorted_stats[0]
second_stat, second_val = sorted_stats[1]

if highest_val - second_val <= 10:
    # append the second emoji
```

You already have a `flavor` dictionary in the function that maps stat names to emojis. You can reuse it or create a second lookup.

---

## How to Test Your Changes

### Quick Terminal Test (Recommended)
Open a terminal in the project folder and run:

```bash
python -c "
from creature import generate_creature
for i in range(8):
    c = generate_creature(f'Creature{i}', 'Forest')
    print(c['avatar'], c['stats'])
"
```

Look for cases where two emojis appear. Try different regions too (`'Volcano'`, `'Ocean'`, `'City'`, etc.).

### Full App Test
```bash
streamlit run app.py
```
Generate several creatures and watch the avatars in the sidebar + main panel.

---

## Success Criteria

You have completed Level 1 when:

- Creatures with one clearly dominant stat still show only two emojis (region + main flavor).
- Creatures whose top two stats are within 10 points show **three** emojis.
- The code is readable and has helpful comments.
- You can explain to someone else *why* you check `highest_val - second_val <= 10`.

---

## Reflection Questions

- What happens if two stats are *exactly* tied for first? Does your code handle it gracefully?
- Would you rather show the second emoji only when the creature is “balanced,” or always show the top two?
- How might you make the rules even more interesting in a future level (for example, special combos for certain regions)?

---

## What’s Next?

Once you finish Level 1, you can:
- Show your favorite creatures to friends
- Try Level 2 (special region + stat combo rules) when it becomes available
- Suggest your own avatar rules!

---

**Remember:** There is no single “correct” answer. The goal is to make the avatar feel more alive and expressive. Have fun and make it yours!

*Created as part of the Creature Generator Educational Lab – June 2026*
