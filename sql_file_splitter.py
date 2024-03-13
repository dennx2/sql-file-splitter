import time

class LargeFile():
    """A class for handling large SQL files."""

    def __init__(self, filePath):
        """
        Initializes a LargeFile object with the given file path.

        Args:
            filePath (str): The path to the large SQL file.
        """
        # Initialize the filePath attribute
        self.filePath = filePath

    def _extract_sql_file(self):
        """
        Extracts SQL commands from the input SQL file.

        Yields:
            str: SQL command segments from the file.
        """
        # Open the file and extract SQL commands
        with open(self.filePath, 'r', encoding='utf-8') as sqlfile:
            buffer = ''
            for line in sqlfile:
                buffer += line
                if line.rstrip().endswith(';'):
                    segment = buffer
                    buffer = ''
                    yield segment.strip()

    def count_command_type(self):
        """
        Counts the occurrences of different types of SQL commands.

        Prints the count of CREATE TABLE, INSERT, and other SQL commands.
        """
        # Initialize counters
        num_create = 0
        num_insert = 0
        num_other = 0

        # Iterate over SQL command segments
        for segment in self._extract_sql_file():
            if 'CREATE TABLE' in segment:
                num_create += 1
            elif 'INSERT' in segment:
                num_insert += 1
            else:
                num_other += 1

        # Print counts
        print(f'CREATE: {num_create}, INSERT: {num_insert}, Other: {num_other}')

    def write_sql_file(self, folderPath):
        """
        Writes SQL commands into separate files based on their types.

        Args:
            folderPath (str): The path to the folder where the output files will be saved.

        Prints the count of CREATE TABLE, INSERT, and other SQL commands, and a message when the writing process is completed.
        """
        # Initialize counters
        count_create = 0
        count_insert = 0
        count_other = 0

        # Iterate over SQL command segments
        for segment in self._extract_sql_file():
            if segment.startswith('CREATE TABLE'):
                count_create += 1
                # Write CREATE TABLE command to file
                with open(f'{folderPath}/create.sql', 'a', encoding='utf-8') as outputFile:
                    outputFile.write(segment)
                    outputFile.write('\n\n')
            elif segment.startswith('INSERT INTO'):
                count_insert += 1
                # Write INSERT command to file
                with open(f'{folderPath}/insert{count_insert//5000+1}.sql', 'a', encoding='utf-8') as outputFile:
                    outputFile.write(segment)
                    outputFile.write('\n\n')
            else:
                count_other += 1
                # Write other SQL commands to file
                with open(f'{folderPath}/other.sql', 'a', encoding='utf-8') as outputFile:
                    outputFile.write(segment)
                    outputFile.write('\n\n')

        # Print counts and completion message
        print(f'CREATE: {count_create}, INSERT: {count_insert}, Other: {count_other}')
        print('Writing Completed')


# Create a LargeFile object with the specified input file path
filePath = 'input/export_clean.sql'
large_file = LargeFile(filePath)

start_time = time.time()

# Specify the output folder for generated SQL files
outputFolder = 'output_sql_files'
large_file.write_sql_file(outputFolder)

end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')


