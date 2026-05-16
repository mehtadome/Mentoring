# Semantic Search Assessment

## Problem

Given an agent-generated claim and a cited text, determine whether the citation actually supports the claim.

This simulates a real problem in production AI systems: agents that retrieve context and cite sources can still hallucinate — either by misrepresenting what a source says or by citing something that doesn't actually support the claim. This function is the verification layer.

## Function Contract

**Entry point:** `index.py → solution(input: dict) -> bool`

**Input:**
```python
{
    'agentText': str,   # claim made by the agent
    'citedText': str    # text cited as evidence
}
```

**Output:** `True` if the cited text supports the claim, `False` if it contradicts or does not support it.

**Constraints:**
- Standard Python only — no external libraries
- Target: under 10ms per call
- Must handle invalid inputs gracefully (empty strings, wrong types, missing keys)
- Use lightweight heuristics: keyword overlap, negation checks, number matching

## Examples

| agentText | citedText | Expected |
|---|---|---|
| "The Earth orbits the Sun." | "The Earth orbits the Sun at an average distance of 93 million miles." | `True` |
| "Vitamin C cures the common cold." | "Scientific studies have conclusively shown that vitamin C does not cure the common cold." | `False` |
| "Mount Everest is the tallest mountain in the world." | "The Pacific Ocean is the largest ocean on Earth." | `False` |

## Test Suite

13 tests in escalating difficulty. Candidates are not expected to pass all of them — each additional test passed is a stronger signal.

| Range | Difficulty | Focus |
|---|---|---|
| 1–2 | Easy | Basic exact match and similarity |
| 3–4 | Easy-Medium | Number matching, partial information |
| 5–6 | Medium | Contradiction detection, logical implication |
| 7–8 | Medium-Hard | Complex multi-concept scenarios |
| 9–11 | Hard | Minimal overlap, edge cases |
| 12 | Very Hard | Real-world complexity |
| 13 | — | Invalid input handling |

## Running

```bash
python index.py
```

## Time Expectations

Aim for 2 hours; do not exceed 4. Code quality and problem-solving approach matter more than a perfect score.

## Deliverables

1. **Code** — debug and improve the helper functions in `index.py` to pass more tests
2. **Video** (5–10 min) — walk through your approach, key challenges, trade-offs made, and how you would extend this in a production environment without the given constraints
