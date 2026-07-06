import os
import random
import sys

def main():
    words_file = os.path.join("resources", "WRDS.txt")
    correct_file = os.path.join("resources", "correct-answers.txt")
    incorrect_file = os.path.join("resources", "incorrect-answers.txt")

    # Step 1 of save-skill: delete existing files and create new ones
    for file_path in [correct_file, incorrect_file]:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
        
        # Ensure directories exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # Create a new empty file
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                pass
        except Exception as e:
            print(f"Error creating {file_path}: {e}")

    # Read and parse the words from resources/WRDS.txt
    if not os.path.exists(words_file):
        print(f"Error: {words_file} not found.")
        sys.exit(1)

    words_list = []
    with open(words_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if ":" not in line:
                continue
            word, definition = line.split(":", 1)
            words_list.append((word.strip(), definition.strip()))

    if len(words_list) < 4:
        print("Error: The words file must contain at least 4 words for multiple choice questions.")
        sys.exit(1)

    correct_count = 0
    incorrect_count = 0

    print("--- GRE Vocabulary Test Agent ---")
    print("Type A, B, C, or D to answer.")
    print("Type 'exit' or 'quit' or 'q' to end the test.\n")

    try:
        while True:
            # Select 1 random word
            target_word, target_def = random.choice(words_list)

            # Select 3 other random words
            other_words = []
            while len(other_words) < 3:
                candidate = random.choice(words_list)
                if candidate[0] != target_word and candidate not in other_words:
                    other_words.append(candidate)

            # Define options (correct definition + 3 distractors)
            options = [target_def] + [d for w, d in other_words]
            random.shuffle(options)

            # Find the correct answer label (A, B, C, D)
            correct_index = options.index(target_def)
            correct_label = chr(65 + correct_index) # 'A', 'B', 'C', 'D'

            # Present the question
            print(f"Please select correct definition of {target_word} :")
            print(f"A) {options[0]}")
            print(f"B) {options[1]}")
            print(f"C) {options[2]}")
            print(f"D) {options[3]}")

            # Take user's answer
            while True:
                user_input = input("> ").strip().upper()
                if user_input in ["EXIT", "QUIT", "Q"]:
                    # Show results in the exact requested form
                    print(f"\n{correct_count} correct answers")
                    print(f"{incorrect_count} incorrect answers")
                    return
                elif user_input in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D, or 'exit'/'quit' to end.")

            # Check user answer and save to files
            if user_input == correct_label:
                correct_count += 1
                with open(correct_file, "a", encoding="utf-8") as f:
                    f.write(f"{target_word}: {target_def}\n")
            else:
                incorrect_count += 1
                with open(incorrect_file, "a", encoding="utf-8") as f:
                    f.write(f"{target_word}: {target_def}\n")
            
            print() # Print empty line for spacing between questions
            
    except KeyboardInterrupt:
        print(f"\n\n{correct_count} correct answers")
        print(f"{incorrect_count} incorrect answers")

if __name__ == "__main__":
    main()
