Ducky Script Generator
This script generates a Ducky Script that simulates human typing by writing the contents of an input text file continuously until the USB device is unplugged.

  Prerequisites
Python 3.x installed on your system
A text editor to create the input text file
A USB Rubber Ducky or a compatible device to run the generated Ducky Script
How to Use

  Step 1: Prepare the Input File
Create a text file named input.txt.
Write the text you want the Ducky Script to type out. Each line in the text file will be typed out by the script.

  Step 2: Download and Run the Python Script
Copy the provided Python script into a file named generate_ducky_script.py.
python



Run the Python script to generate the Ducky Script file (inject.txt):
  python generate_ducky_script.py

The script will read the contents of input.txt and generate inject.txt with the Ducky Script commands.

  Step 3: Load the Ducky Script onto the USB Device
Copy the generated inject.txt file to the root directory of your USB Rubber Ducky or compatible device.
Ensure that your device is set up to run Ducky Script files from inject.txt.

  Step 4: Execute the Ducky Script
Insert the USB Rubber Ducky into the target computer.
The script will begin typing out the contents of input.txt continuously, simulating human typing.
The script will repeat the typing until the device is unplugged.

  Customization
Delay Between Keystrokes: You can adjust the delay between each keystroke by changing the delay variable in the Python script. The default is set to 200 milliseconds.
Delay Between Repetitions: Adjust the delay between each cycle of typing by modifying the f.write(f"DELAY {delay * 10}\n") line in the Python script.

  Notes
Ensure you have permission to use the USB Rubber Ducky on the target system.
Be mindful of the text content and its potential impact on the target system.
Troubleshooting
If the script does not run as expected, verify that the input.txt file is in the correct format and the path is correctly specified.
Check that the USB Rubber Ducky is properly configured to execute Ducky Scripts.
