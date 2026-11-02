from lower_strip import InputsTracker
inputs = InputsTracker()

while True:
    inputs.ask("Enter something (or type 'exit' to quit): ")
    
    if inputs.any == "exit":
        print("\nExiting the program.")
        break

    elif inputs.all == "test":
            print("\nAll inputs were 'test'")
    
    else:
        print("\nRandom else statement hit\n")
    

    inputs.reset() 