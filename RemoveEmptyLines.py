import os


def remove_empty_lines(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()

  # Remove empty lines
  lines = [line.strip() for line in lines if line.strip()]

  with open(filename, 'w') as file:
    file.write('\n'.join(lines))


def remove_empty_lines_in_directory(directory):
  for filename in list(filter(lambda x: "profile" in x or "file" in x,
                              os.listdir(directory))):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
      remove_empty_lines(filepath)


# Replace 'directory_path' with the path to your directory
directory_path = './output'
remove_empty_lines_in_directory(directory_path)
