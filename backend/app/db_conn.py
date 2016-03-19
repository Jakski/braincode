import pg8000

conn = pg8000.connect(host='51.254.113.72', user="braincode", password="brainfuck", database='driny', socket_timeout=100, port=5432)


def selectFrom(sqlScript):
    cursor = conn.cursor()
    cursor.execute(sqlScript)
    val = cursor.fetchall()
    conn.commit()
    return str(val)


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
        sqlScript = "select * from type where name = name"
    else:
        sqlScript = "select * from type where id_type = id"
    return selectFrom(sqlScript)



if __name__ == "__main__":
    dbInsertType("Wino")
    print(dbSelectType("0", "0"))
    print('stop')
