import subprocess

result = subprocess.run(["python3", "script.py"], capture_output=True, text=True)
print(result.stdout)

result = subprocess.run(["python3", "-c", "print([i for i in range(50)])"], capture_output=True, text=True)
print(result.stdout)
