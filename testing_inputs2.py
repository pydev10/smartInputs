from inputs_lower import InputsTracker

try:
    def test_input_tracker_lower():
        inputs = InputsTracker()

        inputs.history = ["Test", "TEST", "test"]
        assert inputs.all == "test"
        assert inputs.all == "TeSt"
        assert inputs.any == "TEST"

        inputs.history = ["hello", "TeSt", "goodbye"]
        assert inputs.any == "test"
        assert inputs.any == "TEST"
        assert inputs.all != "test"

        inputs.history = ["Exit", "eXiT"]
        assert inputs.any == "exit"
        assert inputs.all == "EXIT"

        inputs.reset()
        assert inputs.history == []
        assert inputs.any != "test"
        assert inputs.all != "test"


    if __name__ == "__main__":
        test_input_tracker_lower() 
        print("TEST 2: PASSED")
    
except AssertionError as e:
    print(f"TEST 2: FAILED - {e}")
    