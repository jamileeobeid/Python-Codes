import subprocess

compilation_result = subprocess.run(["g++", "hello.cpp"], capture_output=True, text=True)
print(compilation_result.stdout)

execution_result = subprocess.run(["./a.out"], capture_output=True, text=True)
print(execution_result.stdout)
