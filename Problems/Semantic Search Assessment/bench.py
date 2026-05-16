import time
import index

tests = [
    (1,  "Easy - Simple exact match",              index.test_1,       True),
    (2,  "Easy - Basic similarity",                index.test_2,       True),
    (3,  "Easy-Medium - Number matching",          index.test_3,       True),
    (4,  "Medium - Partial information",           index.test_4,       True),
    (5,  "Medium - Contradiction detection",       index.test_5,       False),
    (6,  "Medium - Logical implication",           index.test_6,       True),
    (7,  "Medium-Hard - Multiple numbers",         index.test_7,       True),
    (8,  "Medium-Hard - Complex similarity",       index.test_8,       True),
    (9,  "Hard - Minimal overlap",                 index.test_9,       True),
    (10, "Hard - Complex contradiction",           index.test_10,      False),
    (11, "Hard - Multiple logical implications",   index.test_11,      True),
    (12, "Very Hard - Complex real-world",         index.test_12,      True),
    (13, "Invalid Input Handling",                 index.invalid_input, False),
]

def run_bench(iterations=100, filter=None):
    subset = [t for t in tests if filter is None or t[0] in filter]
    print(f"{'#':<4} {'Result':<6} {'Avg':>8}  {'Description'}")
    print("-" * 60)
    passed = 0
    for num, desc, data, expected in subset:
        times = []
        result = None
        for _ in range(iterations):
            start = time.perf_counter()
            try:
                result = index.solution(data)
            except Exception:
                result = None
            times.append(time.perf_counter() - start)
        avg_ms = (sum(times) / len(times)) * 1000
        ok = result == expected
        if ok:
            passed += 1
        status = "PASS" if ok else "FAIL"
        print(f"{num:<4} {status:<6} {avg_ms:>6.3f}ms  {desc}")
    print("-" * 60)
    print(f"     {passed}/{len(subset)} passed  (avg over {iterations} iterations each)")

if __name__ == "__main__":
    import sys
    filter = [int(n) for n in sys.argv[1:]] or None
    run_bench(filter=filter)
