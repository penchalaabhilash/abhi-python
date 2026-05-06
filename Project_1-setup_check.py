import sys
print("Welcome to Python Setup Checker")
name= input("Enter your name: ").strip()
print (f"Hello, {name}!")
python_version = sys.version_info
print(f"Python version detected: {python_version.major}.{python_version.minor}.{python_version.micro}")
print("Environment Ready. You can start building projects.")

