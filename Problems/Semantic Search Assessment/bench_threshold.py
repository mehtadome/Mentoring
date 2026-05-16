import time
import index

tests = [
    (1,  "Easy - Simple exact match",              index.test_1,        True),
    (2,  "Easy - Basic similarity",                index.test_2,        True),
    (3,  "Easy-Medium - Number matching",          index.test_3,        True),
    (4,  "Medium - Partial information",           index.test_4,        True),
    (5,  "Medium - Contradiction detection",       index.test_5,        False),
    (6,  "Medium - Logical implication",           index.test_6,        True),
    (7,  "Medium-Hard - Multiple numbers",         index.test_7,        True),
    (8,  "Medium-Hard - Complex similarity",       index.test_8,        True),
    (9,  "Hard - Minimal overlap",                 index.test_9,        True),
    (10, "Hard - Complex contradiction",           index.test_10,       False),
    (11, "Hard - Multiple logical implications",   index.test_11,       True),
    (12, "Very Hard - Complex real-world",         index.test_12,       True),
    (13, "Invalid Input Handling",                 index.invalid_input, False),
]

THRESHOLDS = [0.50, 0.60, 0.75, 0.90]

def make_solution(threshold):
    """Return a patched solution using the given overlap threshold."""
    def solution(input):
        try:
            agent_text = input['agentText']
            cited_text = input['citedText']
            if not isinstance(agent_text, str) or not isinstance(cited_text, str):
                return False
            agent_text = agent_text.strip()
            cited_text = cited_text.strip()
            if not agent_text or not cited_text:
                return False
        except (KeyError, TypeError, AttributeError):
            return False

        agent_text_tokens = [x for x in index.remove_irrelevant_words(agent_text).split(' ') if x != '']
        cited_text_tokens = [x for x in index.remove_irrelevant_words(cited_text).split(' ') if x != '']
        agent_numbers = index.extract_numbers_from_text(agent_text)
        cited_numbers = index.extract_numbers_from_text(cited_text)
        similarity = index.get_semantic_similarity(agent_text_tokens, cited_text_tokens)
        has_range_match = index.has_numerical_range_match(agent_numbers, cited_numbers)

        if index.has_contradiction(agent_text_tokens, cited_text_tokens):
            return False
        if index.has_exact_match(agent_text_tokens, cited_text_tokens):
            return True
        if len(similarity) > 1:
            return has_range_match or False if index.has_partial_information(agent_text_tokens, similarity) else True
        if has_range_match:
            return True
        if index.has_logical_implication(agent_text_tokens, cited_text_tokens, threshold):
            return True

        return False
    return solution

def run_threshold_bench(iterations=100):
    col_w = 36
    print(f"{'#':<4} {'Description':<{col_w}}", end="")
    for t in THRESHOLDS:
        print(f"  {int(t*100)}%  ", end="")
    print()
    print("-" * (4 + col_w + len(THRESHOLDS) * 8 + 2))

    total_passed = {t: 0 for t in THRESHOLDS}

    for num, desc, data, expected in tests:
        print(f"{num:<4} {desc:<{col_w}}", end="")
        for threshold in THRESHOLDS:
            solution = make_solution(threshold)
            result = None
            for _ in range(iterations):
                try:
                    result = solution(data)
                except Exception:
                    result = None
            ok = result == expected
            if ok:
                total_passed[threshold] += 1
            status = "PASS" if ok else "FAIL"
            print(f"  {status}", end="")
        print()

    print("-" * (4 + col_w + len(THRESHOLDS) * 8 + 2))
    print(f"{'':4} {'TOTAL':<{col_w}}", end="")
    for t in THRESHOLDS:
        print(f"  {total_passed[t]}/{len(tests)} ", end="")
    print()

if __name__ == "__main__":
    run_threshold_bench()
