import pg8000

conn = pg8000.connect(host='51.254.113.72', user="braincode", password="brainfuck", database='driny', socket_timeout=100, port=5432)


def selectFrom(sqlScript):
    cursor = conn.cursor()
    cursor.execute(sqlScript)
    val = cursor.fetchall()
    conn.commit()
    return val


def insertInto(sqlScript):
    cursor = conn.cursor()
    cursor.execute(sqlScript)
    conn.commit()


def dbInsertTool(name, description):
    sqlScript = "INSERT INTO tool(name, description)VALUES ('{a}', '{b}');".format(a=name, b=description)
    insertInto(sqlScript)


def dbSelectTool(id):
    if id == "0":
        sqlScript = "select * from tool"
    else:
        sqlScript = "select * from tool where id_tool = {a}".format(a=id)
    return selectFrom(sqlScript)


def dbInsertType(name):
    sqlScript = "INSERT INTO type(name) VALUES ('{a}');".format(a=name)
    insertInto(sqlScript)


def dbSelectType(id, name):
    if id == "0" and name == "0":
        sqlScript = "select * from type"
    elif id == "0":
        sqlScript = "select * from type where name = {a}".format(a=name)
    else:
        sqlScript = "select * from type where id_type = {a}".format(a=id)
    return selectFrom(sqlScript)


def dbInsertHash(hash):
    sqlScript = "INSERT INTO hash(hash) VALUES ('{a}');".format(a=hash)
    insertInto(sqlScript)


def dbSelectHash(id, hash):
    if id == "0" and hash == "0":
        sqlScript = "select * from hash"
    elif id == "0":
        sqlScript = "select * from hash where hash = '{a}'".format(a=hash)
    else:
        sqlScript = "select * from hash where id = '{a}'".format(a=id)
    return selectFrom(sqlScript)


def dbInserAlco(id_hash, id_type, name, manufacturer):
    sqlScript = "INSERT INTO alco(id_hash, id_type, name, manufacturer) VALUES('{a}', '{b}', '{c}', '{d}'');".format(a=id_hash, b=id_type, c=name, d=manufacturer)
    insertInto(sqlScript)


def dbSelectAlco(id_hash, id_type):
    if id_hash == "0" and id_type == "0":
        sqlScript = "select * from alco "
    elif id_hash == "0":
        sqlScript = "select * from alco where id_type = {a}".format(a=id_type)
    else:
        sqlScript = "select * from alco where id_hash = {b}".format(b=id_hash)
    return selectFrom(sqlScript)

if __name__ == "__main__":
    print(dbSelectType("0", "0"))
    print('stop')
