from inputs_lower import InputsTracker


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

    print("All lowercase input tracker checks passed.")


if __name__ == "__main__":
    test_input_tracker_lower()
