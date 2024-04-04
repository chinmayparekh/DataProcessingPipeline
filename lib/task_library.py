import pandas as pd

def display(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()
        print(content)

        with open(output_file_path, 'w') as output_file:
            output_file.write(content)

def slice(input_file_path, output_file_path, column_name):
    df = pd.read_excel(input_file_path)
    sliced = df[column_name]

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(sliced))

def dice(input_file_path, output_file_path, column_names):
    print(column_names)
    df = pd.read_excel(input_file_path)
    diced = df[column_names]

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(diced))

def remove_nulls(input_file_path, output_file_path):
    df = pd.read_excel(input_file_path)
    no_nulls = df.dropna()

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(no_nulls))

def upper(input_file_path, output_file_path, column_name):
    df = pd.read_excel(input_file_path)
    df[column_name[0]] = df[column_name[0]].str.upper()

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(df))

def mean(input_file_path, output_file_path, column_name):
    df = pd.read_excel(input_file_path)
    mean = df[column_name].mean()

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(mean))

