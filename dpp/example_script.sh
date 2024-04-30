#!/bin/bash

# Usage: ./example_script.sh input_file output_file

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 input_file output_file"
    exit 1
fi

# Assign arguments to variables
input_file=$1
output_file=$2

# Process the input file and write to output file
while IFS= read -r line; do
    # Convert each line to uppercase and write to the output file
    echo "$line" | tr '[:lower:]' '[:upper:]' >> "$output_file"
done < "$input_file"

# Print a message indicating the script has completed successfully
echo "Processing complete. Output written to $output_file."
