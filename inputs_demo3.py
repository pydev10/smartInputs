from lower_strip import InputsTracker
inputs = InputsTracker()

while True:
    user_input = inputs.ask("Enter something (or type 'exit' to quit): ")
    if user_input is None:
        break  # Exit on KeyboardInterrupt
    if user_input.strip().lower() == "exit":
        print("Exiting the input tracker.")
        break

    print(f"You entered: {user_input}")
    print(f"Current history: {inputs.history}")
    print(f"All inputs match 'test': {inputs.all == 'test'}")
    print(f"Any input matches 'test': {inputs.any == 'test'}")

    inputs.reset() 