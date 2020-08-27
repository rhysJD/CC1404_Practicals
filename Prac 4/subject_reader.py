"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    for i in range(0, len(data)):
        print("{:6} is taught by {:15} and has {:3} students".format(data[i][0], data[i][1], data[i][2]))

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts_list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        parts_list.append(parts)
    input_file.close()
    return parts_list

main()
