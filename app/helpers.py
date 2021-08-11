from bson.objectid import ObjectId
#helper function to convert object id
def  objidconv(inp):
    dic={}
    for keys,values in inp.items():
        if (keys=='uname' or keys=='posts' or keys=='groups' or keys=='last_login'):
            dic[keys]=values
    return dic