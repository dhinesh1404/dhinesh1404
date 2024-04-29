msg = "start programe"
print(msg)

def bar(argB1, argB2):
    msg1 = "hello!" + foo(argB1)
    print(msg1)
    
    msg2 = "hello!" + foo(argB2)
    print(msg2)
    

def foo(argF):
    msg = argF + "."
    msg = pos(msg)
    return msg

def pos(argP):
    msg = "*" + argP + "*"
    return msg

bar("dhinesh", "sd kumar")

msg = "end program"
print(msg)