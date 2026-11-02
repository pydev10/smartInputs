from inputs_strip import InputsTracker
inputs = InputsTracker()

while True:
    user_input1 = inputs.ask("Type anything ('exit' to quit): ")
    user_input2 = inputs.ask("Type anything ('exit' to quit): ")
    if inputs.any == "exit":
        print("\nExiting")
        break

    elif inputs.all == "test":
        print("\nAll inputs were 'test'")

    else:
        print("\nRandom else statement hit\n")

    inputs.reset()