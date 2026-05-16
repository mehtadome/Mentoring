class Solution:
    def maxScore(self, arr: list[int], k: int) -> int:
        """
        Given an integer array arr and integer k, partition arr into exactly k
        non-empty contiguous subarrays. The score of a partition is the sum of
        (max - min) for each subarray. Return the maximum score.

        Example 1:
            arr = [5, 1, 4, 2, 3], k = 2
            Partition [5, 1] | [4, 2, 3] gives (5-1) + (4-2) = 4 + 2 = 6
            Output: 6

        Example 2:
            arr = [1, 10, 1, 10], k = 2
            Partition [1, 10] | [1, 10] gives 9 + 9 = 18
            Output: 18
        """
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([5, 1, 4, 2, 3], 2, 6),    
        ([1, 5], 1, 4),               
        ([1, 5], 2, 0),               
        ([1], 1, 0),                  
        ([1, 2, 3, 4, 5], 1, 4),     
        ([1, 2, 3, 4, 5], 5, 0),    
        ([1, 10, 1, 10], 2, 18),    
        ([3, 1, 4, 1, 5, 9, 2, 6], 3, 15),  
    ]

    passed = 0
    for arr, k, expected in tests:
        try:
            result = sol.maxScore(arr, k)
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                passed += 1
            print(f"{status}  arr={arr}, k={k}  expected={expected}, got={result}")
        except NotImplementedError:
            print(f"SKIP  arr={arr}, k={k}  (not implemented)")

    print(f"\n{passed}/{len(tests)} passed")
