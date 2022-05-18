# Solicite un valor al usuario y confirme que sea mayor que 0
def checkvalue(valuetocheck): 
    assert (type(valuetocheck) is int), "You must enter anumber." 
    assert (valuetocheck > 0), "Value entered must be greaterthan 0" 
    if valuetocheck > 4: 
        print("Value is greater than 4")
var = int(input("Enter a number greater than 0: ")) 
checkvalue(var)