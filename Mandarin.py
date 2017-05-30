def convert_to_mandarin(us_num):
    '''
   us_num, a string representing a US number 0 to 99
   returns the string mandarin representation of us_num
   '''
   
    num = int(us_num)  
    small = num%10  
    big = (num - small) // 10  
    translated = ""    
   
    if num <= 10:
        if num is 10:
            translated += trans['10']
        else:
            translated += trans[str(small)]  
    elif num > 10 and num < 20:
        translated += "shi " + trans[str(small)]
    else:
        translated += trans[str(big)] + " shi "
        if small is not 0:
            translated+=  trans[str(small)]
   
    return translated.strip()