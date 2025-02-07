
def func() :
    name="pramod"  # variable created in function
output=func()
print(output) # It will return None bevuase ' return ; keyword not used

def func() :
    name="pramod"  # variable created in function
    return name  # return with variable
output=func()
print(output)