import ctypes

ctypes.cdll.LoadLibrary('./libvalidate.so')
validate = ctypes.CDLL('./libvalidate.so')

print(validate)

validate.validate_block.argtypes = [ctypes.c_int]

def validate_block(n):
    # testing calling C functions with ctypes
    global validate
    return validate.validate_block(ctypes.c_int(n))
