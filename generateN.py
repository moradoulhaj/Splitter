import sys


def generate_numbers(n, filename):
  with open(filename, 'w') as file:
    for num in range(1, n + 1):
      file.write(f"{num}\n")


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python script_name.py <n> <filename>")
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("Error: n must be an integer.")
    sys.exit(1)

  filename = sys.argv[2]

  generate_numbers(n, filename)
