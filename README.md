# SQL File Splitter Script

This script is designed to process large SQL files, extracting SQL commands, counting their occurrences, and writing them into separate files based on their types.

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. **Download the script**: 
- Download the `sql_file_splitter.py` script from the repository.

2. **Prepare your SQL file**: 
- Ensure you have a large SQL file that you want to process. The file should be in UTF-8 encoding.

3. **Modify script variables**: 
- Modify the `filePath` variable in the script to specify the path to your input SQL file.
- Modify the `outputFolder` variable to specify the path to the output folder where the generated SQL files will be saved.
- If your input file is not encoded in UTF-8, you can change the encoding in the `_extract_sql_file()` method of the `LargeFile` class accordingly.

4. **Run the script**: 
- Open a terminal or command prompt, navigate to the directory containing the script, and execute the following command:

    ```bash
    python sql_file_splitter.py
    ```

5. **Wait for processing to complete**: 
- The script will begin processing the SQL file, extracting commands, counting their occurrences, and writing them into separate files. The processing time may vary depending on the size of the input file.

6. **Check output files**: 
- Once the processing is complete, check the specified output directory (default: `output_sql_files`) for the generated SQL files.

## Example

```python

# Specify the path to your SQL file
filePath = 'input/export_clean.sql'

# Initialize LargeFile object
large_file = LargeFile(filePath)

# Measure execution time
start_time = time.time()

# Write SQL files based on command types
outputFolder = 'output_sql_files'
large_file.write_sql_file(outputFolder)

# Measure execution time
end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')
```

## Note

- Ensure that you have sufficient disk space available in the output directory, as the generated files may be large, especially for large input SQL files.
- If your input file is not encoded in UTF-8, you can change the encoding in the `_extract_sql_file()` method of the `LargeFile` class by modifying the `encoding` parameter in the `open()` function call.
- It's important to choose the correct encoding to accurately read the file content.
- Additionally, the code can be modified to execute SQL commands directly on connected servers like MySQL or SQL Server. This would involve replacing or modifying the `write_sql_file()` method to execute the commands using appropriate database drivers or libraries.

