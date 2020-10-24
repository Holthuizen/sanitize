def sanitize(inputstr):
    sanitized = ''
    bad_characters = [
        ';',
        '*',
        '<',
        '>',
        '\'',
        '1,2',
        '`',
        '(',
        ')',
    ]
    bad_strings=[
        'file://',
        'input://',
        '../',
        '\x00',
        '%3C',
        '--',
        '&&',
        '\'',
    ]
    #remove all dangerous chars. 
    for char in inputstr:  
        sanitized += '' if (char in bad_characters) else char 
    #now replace dangerous strings with a non dangerous char. (if you remove instead you get: f--le:// -> file://)
    for s in bad_strings:
        try:
            sanitized = sanitized.replace(s,'?')
        except:
            pass
    return sanitized.strip(' ')

'''
python function for some what save input sanitazion. 
origin :  dustyfresh/sanitize.py  
#print(sanitize("  && hello %3C&'& world")) -> ? hello ?? world
'''
