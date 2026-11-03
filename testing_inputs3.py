from inputs_strip import InputsTracker

try:
    def test_input_tracker_strip():
        inputs = InputsTracker()

        inputs.history = ["  test  ", "test", "test  "]
        assert inputs.all == "test"
        assert inputs.any == "test"

        inputs.history = ["hello", "  test  ", "goodbye"]
        assert inputs.any == "test"
        assert inputs.all != "test"

        inputs.history = ["  exit  ", "exit"]
        assert inputs.any == "exit"
        assert inputs.all == "exit"

        inputs.reset()
        assert inputs.history == []

        

    if __name__ == "__main__":
        test_input_tracker_strip()
        print("TEST 3: PASSED")
        
except AssertionError as e:
    print(f"TEST 3: FAILED - {e}")
