def bar():
    msg1 ="<<" + name
    
    msg2 = foo(msg1)
    msg2 += " "
    
    msg3 = pos(msg2)
    msg3 += " "
    
    return msg3

def foo(argF):
    msg = argF + "."
    return msg

def pos(argP):
    msg = argP + "Hello"
    return(msg)

name = "dhinesh"

result = bar()

print(result)