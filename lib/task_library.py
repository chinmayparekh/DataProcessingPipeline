# task_library.py

def display(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()
        print(content)

        with open(output_file_path, 'w') as output_file:
            output_file.write(content)

# Add more functions as needed