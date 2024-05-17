#!/usr/bin/python3
"""
Log Parsing Script
This script reads log data from standard input (stdin), parses the log entries,
and tracks the frequency of various HTTP status codes and the cumulative file
size of all processed log entries. The script prints the cumulative file size
and status code counts after every 10 lines processed and upon termination
(normal or via KeyboardInterrupt).
Log entries are expected to have a format that includes HTTP status codes and
file sizes. The supported HTTP status codes being tracked are:
- 200: OK
- 301: Moved Permanently
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 405: Method Not Allowed
- 500: Internal Server Error
"""

import re
import sys

# Initialize line counter and total file size
line_counter = 0
total_file_size = 0

# Dictionary to keep count of each status code
status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0,
                      405: 0, 500: 0}

def print_status_counts(status_counts, file_size):
    """
    Prints the total file size and the count of each HTTP status code.
    Args:
        status_counts (dict): A dictionary with HTTP status codes as
        keys and their counts as values.
        file_size (int): The cumulative size of files processed.
    """
    # Print the total file size
    print("File size: {}".format(file_size))
    # Print each status code and its count if the count is not zero
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] != 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

if __name__ == "__main__":
    try:
        # Read each line from the standard input
        for line in sys.stdin:
            # Split the line using regular expression to
            # isolate status code and file size
            split_line = re.split(r'- |"|"| " " ', str(line))
            # Get the last part of the split line which contains
            # status code and file size
            status_code_and_file_size = split_line[-1]
            # Print status counts and file size every 10 lines
            if line_counter != 0 and line_counter % 10 == 0:
                print_status_counts(status_code_counts, total_file_size)
            line_counter += 1
            try:
                # Extract status code and file size from the split part
                status_code = int(status_code_and_file_size.split()[0])
                file_size = int(status_code_and_file_size.split()[1])
                # Update the count for the status code if it is being tracked
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                # Add the file size to the total file size
                total_file_size += file_size
            except (IndexError, ValueError):
                # Skip the line if there is an error in extracting
                # status code or file size
                pass
        # Print the final counts after all lines are processed
        print_status_counts(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        # Print the final counts if the script is interrupted by the user
        print_status_counts(status_code_counts, total_file_size)
        raise
