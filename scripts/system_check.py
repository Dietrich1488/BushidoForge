import os
import platform
import sys

print("=== BushidoForge System Check ===")

print(f"User: {os.getlogin()}")
print(f"Hostname: {platform.node()}")
print(f"OS: {platform.system()}")
print(f"Kernel: {platform.release()}")
print(f"Current directory: {os.getcwd()}")
print(f"Python: {sys.version.split()[0]}")

print("==============================")

