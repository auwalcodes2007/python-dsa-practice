import time

def evaluate_test_case(func, test, display=True):
    """
    Evaluates a function against a single test case dictionary.
    Returns: (actual_output, passed_boolean, execution_time_ms)
    """

    inputs = test["input"]
    expected = test["output"]

    start_time = time.perf_counter()
    actual = func(**inputs)
    elapsed_ms = (time.perf_counter() - start_time) * 1000 # in milliseconds

    passed = actual == expected
    status = "✅ PASSED" if passed else "❌ FAILED"

    if display:
        print(f"Status:   {status} ({elapsed_ms:.3f} ms)")
        print(f"Input:    {inputs}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}\n")

    return actual, passed, elapsed_ms 



        