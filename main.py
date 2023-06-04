def repeat_text(input_file, output_file, repetitions):
    try:
        with open(input_file, 'r') as file:
            text = file.read()

        with open(output_file, 'w') as file:
            for _ in range(repetitions):
                file.write(text + '\n')
    except IOError:
        print("An error occurred while reading or writing the file.")


input_file = "text.txt"
output_file = "output.txt"
repetitions = 100


repeat_text(input_file, output_file, repetitions)
