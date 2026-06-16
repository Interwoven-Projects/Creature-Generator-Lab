"""
creature.py — Logic layer for the Creature Generator educational lab.
This file contains ZERO Streamlit code so it can be imported and tested
in plain Python or Jupyter. All generation is deterministic given a seed.

Teaching goals:
- Separation of concerns (logic vs presentation)
- Data-driven design (regions.json)
- Procedural generation with explicit seeds (reproducibility)
- SQT-inspired Unique Time Calculator for thematic "birth moment"
"""

import json
import random
import hashlib
from datetime import datetime
from typing import Any, Dict


def load_regions(json_path: str = "regions.json") -> Dict[str, Any]:
    """Load region modifiers and descriptions from JSON file."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_sqt_inspired_seed() -> int:
    """
    Unique Time Calculator (SQT-inspired).
    Returns a changing integer based on current wall-clock time.
    This gives creatures a "born at this moment" feeling without
    requiring students to understand the full 37.3-hour quantum day yet.

    Full SQT library (lunar-synchronized 19-day lunations, themed moons):
    https://github.com/Squirrel814/Squirrel-Quantum-Time

    Students can later replace this with real SQT calls for moon-phase
    rarity or special "forage event" traits.
    """
    # Use timestamp() for sub-millisecond resolution — more reliable
    # for successive calls during demos and testing.
    now = datetime.now().timestamp()
    tick = int(now * 1_000_000) % 1_000_000
    return tick


def generate_creature(
    name: str,
    region: str,
    custom_seed: int | None = None
) -> Dict[str, Any]:
    """
    Main creature generation function.

    Deterministic: same inputs + same seed → same creature.
    When custom_seed is None, mixes:
      - Hash of creature name (personalization)
      - Current SQT-inspired time tick (uniqueness / "birth moment")
      - Region (thematic consistency)
    """
    regions = load_regions()
    if region not in regions:
        available = ", ".join(regions.keys())
        raise ValueError(f"Unknown region '{region}'. Available: {available}")

    region_data = regions[region]
    modifiers = region_data["modifiers"]

    # --- Seed calculation (core teaching moment) ---
    if custom_seed is not None:
        seed = int(custom_seed)
    else:
        name_hash = int(hashlib.sha256(name.encode("utf-8")).hexdigest(), 16) % 100_000
        time_tick = get_sqt_inspired_seed()
        # Mix name + time + simple region hash for good distribution
        region_bonus = sum(ord(c) for c in region) % 1000
        seed = (name_hash + time_tick + region_bonus) % 1_000_000

    random.seed(seed)

    # Base stats before region modifiers (simple, learnable range)
    base_stats: Dict[str, int] = {
        "strength": random.randint(48, 82),
        "speed": random.randint(48, 82),
        "intelligence": random.randint(48, 82),
        "creativity": random.randint(48, 82),
        "charm": random.randint(48, 82),
    }

    # Apply region modifiers (the "environment shapes the creature" lesson)
    final_stats: Dict[str, int] = {}
    for stat, base_val in base_stats.items():
        mod = modifiers.get(stat, 1.0)
        final_stats[stat] = max(12, round(base_val * mod))

    # Visual & flavor
    avatar = _choose_avatar(region, final_stats)
    description = _build_description(name, region, final_stats, seed)

    return {
        "name": name,
        "region": region,
        "region_description": region_data["description"],
        "stats": final_stats,
        "avatar": avatar,
        "seed_used": seed,
        "sqt_tick_at_birth": get_sqt_inspired_seed(),  # fresh tick for display
        "description": description,
    }


def _choose_avatar(region: str, stats: Dict[str, int]) -> str:
    """
    STUDENT LAB CHALLENGE — Level 1: Secondary Stat Boost
    =====================================================
    Goal: Make the avatar reflect BOTH the strongest stat AND a close second stat
          when they are very competitive (within ~10 points).

    Why this matters:
    - Teaches finding top-2 values with sorted()
    - Introduces simple conditional logic for "close race" situations
    - Makes creatures feel more nuanced and alive

    Current behavior (what you start with):
    - Only shows region + dominant stat emoji

    Your task:
    1. Find the highest AND second-highest stats
    2. If the difference between them is small (<= 10), append the second emoji too
    3. Test it! Run generate_creature several times and look for interesting combos

    Example ideas you can implement:
    - Forest creature with high creativity + high intelligence → 🌲🧠🎨
    - Volcano with high strength + high creativity → 🌋💪🎨 (magma artist!)

    Stretch goals (optional for now):
    - Add special region + stat combo rules (e.g. Ocean + high charm)
    - Use the seed or SQT tick for rare "shiny" variants later

    Have fun and make it yours!
    """
    region_emoji = {
        "Forest": "🌲", "Mountain": "⛰️", "Ocean": "🌊", "Desert": "🏜️",
        "City": "🏙️", "Tundra": "❄️", "Volcano": "🌋", "Plains": "🌾"
    }.get(region, "🧬")

    # --- Current simple logic (baseline) ---
    highest_stat = max(stats, key=stats.get)
    flavor = {
        "strength": "💪",
        "speed": "⚡",
        "intelligence": "🧠",
        "creativity": "🎨",
        "charm": "✨"
    }.get(highest_stat, "🔮")

    avatar = f"{region_emoji}{flavor}"

    # ============================================
    # STUDENT CHALLENGE STARTS HERE (Level 1)
    # ============================================
    # TODO: Find the second highest stat and decide whether to append its emoji.
    #
    # Hint:
    # sorted_stats = sorted(stats.items(), key=lambda item: item[1], reverse=True)
    # highest_stat, highest_val = sorted_stats[0]
    # second_stat, second_val = sorted_stats[1]
    #
    # Then check: if highest_val - second_val <= 10:
    #     second_flavor = flavor.get(second_stat, "")
    #     if second_flavor:
    #         avatar += second_flavor
    #
    # Delete the TODO comment and write your code below when you're ready!
    # ============================================

    # ============================================
    # LEVEL 2 (Future Challenge - Do after Level 1)
    # ============================================
    # Once Level 1 is working, try adding special combo rules.
    #
    # Examples you can implement:
    # - if region == "Volcano" and highest_stat == "creativity":
    #       avatar = "🌋🔥🎨"   # Magma Forger
    # - if region == "Ocean" and stats.get("intelligence", 0) > 85:
    #       avatar += "🧠"     # Wise current
    #
    # This teaches region + stat synergy rules.
    # A full Level 2 lab page will be added when you're ready.
    # ============================================

    # ============================================
    # LEVEL 3 (Future Challenge - Do after Level 2)
    # ============================================
    # Use the seed_used or sqt_tick_at_birth to create rarity.
    #
    # Ideas:
    # - If seed % 100 < 5  → Legendary (add 👑 or ✨✨)
    # - If seed % 100 < 20 → Rare (add ✨)
    # - Else               → Common
    #
    # You can also return a "rarity" string or add it to the creature dict later.
    # This connects the SQT Unique Time system to visual feedback.
    # ============================================

    return avatar


# ============================================
# LEVEL 4 SCAFFOLDING (Data-Driven Rules)
# ============================================
def load_avatar_rules(path: str = "avatar_rules.json") -> dict:
    """
    LEVEL 4 CHALLENGE
    Load avatar rules from external JSON file.
    
    This is the biggest conceptual step in the lab:
    Moving logic out of Python code and into data files.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# TODO for Level 4:
# 1. Use load_avatar_rules() inside generate_creature or _choose_avatar
# 2. Apply rarity_thresholds from the JSON
# 3. Apply combo_rules from the JSON instead of hard-coded if statements
# 4. Use rarity_visuals for the final avatar decoration
#
# This makes the avatar system fully configurable without editing Python.
# ============================================


def _build_description(name: str, region: str, stats: Dict[str, int], seed: int) -> str:
    """Procedural flavor text. Easy for students to improve with more if/elif."""
    highest = max(stats, key=stats.get)
    traits = {
        "strength": "powerful and sturdy",
        "speed": "quick and agile",
        "intelligence": "clever and observant",
        "creativity": "imaginative and inventive",
        "charm": "charismatic and friendly"
    }
    trait = traits.get(highest, "balanced")

    return (
        f"{name} is a {trait} creature born in the {region.lower()}. "
        f"Its unique SQT birth tick was {seed}. "
        "It carries the essence of its homeland in every step."
    )
