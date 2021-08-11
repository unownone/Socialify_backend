

#helper function to convert object id
def  objidconv(inp):
    for keys in inp:
        if(keys=='_id'):
            inp[keys]=str(inp[keys])
        if(keys!='_id' or keys!='uname' or keys!='posts' or keys!='groups' or keys!='last_login'):
            del inp[keys]
    return inp
