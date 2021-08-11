

#helper function to convert object id
def  objidconv(inp):
    for keys in inp:
        if(keys=='_id'):
            inp[keys]=str(inp[keys])
    return inp
