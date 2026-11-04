# Note: Use the global python interpreter | usr/bin/python3 as it tends to be buggy with the python venv enviroment

# smartInputs project

A clean Python tool to check multiple console text inputs instantly without messy daisy chains.

## Read This Before Using (Project Rules and application of inputs.any)
* **inputs.any:** inputs.any detects if an input matches a string in a list. If it does the condition will evaluate to True.
* **inputs.all:** inputs.all detects if all inputs matches a single string in a list or string after an equality operator
* **Completely Free:** You can copy, change, or use this code anywhere for free.
* **No Responsibility:** This code comes as-is. If you use it and your code breaks, that is on you.
* **No Feature Requests:** I will NOT be implementing extra features (like mathematical integer and float support or auto-casting). The framework is strictly for text.
* **Tweakers Welcome:** If you want new features, tweak the code and add them yourself!
* **Legal Notice (Philippines):** This source code is an original creation protected under Republic Act No. 8293 (Intellectual Property Code of the Philippines). It is distributed globally under the standard MIT License conditions.

* **Tip:** Integers and float are technically supported but treated as strings.
* **Here are 2 examples of the tip:**
if inputs.any in ['1', '2', '3']:
if inputs.all == '1':


## How to use it
## This is for the "inputs_tracker.py" file
```python
# Name a file called "inputs_tracker" in the same folder to import it
import inputs_tracker

inputs = inputs_tracker.InputsTracker()


while True:
    user_word = inputs.ask("Enter a word: ")
    user_word2 = inputs.ask("And another one: ")
    
    
    if inputs.all == "exit":
        print("\nturning off...")
        break
        
    
   
    elif inputs.any in ['programming', 'coding', 'hardware']:
        print('\nthese make computers work! (used to test if code works)')
        
    
    else:
        print(f"'\n{user_word}' is cool but doesn't make computers work.")

    inputs.reset()
