import subprocess

return_code = subprocess.call(["python3", "--version"])
print(return_code)

output = subprocess.check_output(["python3", "--version"], text=True)
print(output)
