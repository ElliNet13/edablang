def interpret_code(code, variables):
  if code.startswith("dab on"):
      value = code[7:].strip()
      if value != "":
          print(value)
  elif code.startswith("play ball"):
      variable_name = code[10:].strip()
      if variable_name in variables:
          print(variables[variable_name])  # Print the variable value
  elif code.startswith("yeetly"):
      _, var_name, value = code.split(" ", 2)
      var_name = var_name.strip()
      value = value.strip()
      variables[var_name] = value

def run_edablang(file_path):
  # Initialize variables dictionary
  variables = {}

  try:
      # Open and read the .edablang file
      with open(file_path, "r") as file:
          lines = file.readlines()

      # Interpret and execute each line of code
      for line in lines:
          interpret_code(line.strip(), variables)

  except FileNotFoundError:
      print(f"Error: File '{file_path}' not found.")
  except Exception as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  import sys

  if len(sys.argv) == 1:
      # Default to script.edablang if no file path provided
      file_path = "main.edablang"
  elif len(sys.argv) == 2:
      # Use the provided file path
      file_path = sys.argv[1]
  else:
      print("Usage: python edablangcompiler.py [file_path]")
      sys.exit(1)

  if not file_path.endswith(".edablang"):
      print("Error: The file must have a .edablang extension.")
      sys.exit(1)

  run_edablang(file_path)
