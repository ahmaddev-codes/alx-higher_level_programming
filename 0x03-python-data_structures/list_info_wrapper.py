from ctypes import cdll, py_object

# Load the C library
lib = cdll.LoadLibrary('./list_info.so')  # Replace with the correct library path

# Define the function prototype
print_python_list_info = lib.print_python_list_info
print_python_list_info.argtypes = [py_object]
print_python_list_info.restype = None

# Define a Python function to call the C function
def print_list_info(p):
    print_python_list_info(p)
