def explode():
    print("BOOM!")
    exit(-1)



def phase3():
    number = [2,11]
    x0= number[0]
    if x0 == 2 :
        w2 = number[1]
        w0 = 0x66666667
        w0 = w2 // 10
        w1 = w2 % 10
        w0 = w1 + w0 = w2 - 9 * (w2 // 10)
        if w0 == 2:
            return
    elif x0 == 5:
        w0 = number[1]
        # some encryption to w0
        w1 = number[0]
        if w1 == w0:
            return
    elif x0 == 1:
        w0 = number[1]
        w1 = number[0]
        w2 = w0 & 0x111
        if w2 == w1:
            return
        else:
            w0 = (w0 >> 3) & 0x7
            if w1 == w0:
                return

def encrypt_method1(input_line, lenth):
    pass

def phase4(input_line):
    x19 = input_line
    w0 = len(input_line)
    x20 = w0
    if w0 <= 12:
        w1 = len(input_line)
        w0 = input_line
        w0, w1 = encrypt_method1(w0, w1) # new line, new len
        w0, w1 = 
        
    