from inputs_lower import InputsTracker
inputs = InputsTracker()

while True:
    inputs.ask("Type anything ('exit' to quit): ")
    inputs.ask("Type anything ('exit' to quit): ")
    if inputs.any == "exit":
        print("\nExiting")
        break

    elif inputs.all == "test":
        print("\nAll inputs were 'test'")

    else:
        print("\nRandom else statement hit\n")

    inputs.reset()