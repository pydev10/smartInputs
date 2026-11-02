from inputs_strip import InputsTracker
inputs = InputsTracker()

while True:
    user_input = inputs.ask("Enter something (or type 'exit' to quit): ")
    user_input2 = inputs.ask("Enter something (or type 'exit' to quit): ")
        
    if inputs.any == "exit":
        print("\nExiting the program.")
        break

    elif inputs.all == "test":
            print("\nAll inputs were 'test'")
    
    else:
        print("\nRandom else statement hit\n")
    

    inputs.reset() 