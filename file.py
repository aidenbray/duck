def generate_ducky_script(input_file, output_file, delay):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write("DELAY 1000\n")  # Initial delay to allow the system to recognize the device

        for line in lines:
            for char in line:
                if char == '\n':
                    f.write("ENTER\n")
                else:
                    f.write(f"STRING {char}\n")
                    f.write(f"DELAY {delay}\n")

if __name__ == "__main__":
    input_file = "input.txt"  # Path to the input text file
    output_file = "inject.txt"  # Path to the output Ducky Script file
    delay = 200  # Delay in milliseconds between each keystroke

    generate_ducky_script(input_file, output_file, delay)
    print(f"Ducky Script generated: {output_file}")
