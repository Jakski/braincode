# -*- coding: utf-8 -*-
import pg8000

conn = pg8000.connect(host='51.254.113.72', user="braincode", password="brainfuck",
                      database='driny', socket_timeout=100, port=5432)


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
        sqlScript = "select * from tool where id_tool = '{a}'".format(a=id)
    return selectFrom(sqlScript)




def dbInsertType(name):
    sqlScript = "INSERT INTO type(name) VALUES ('{a}');".format(a=name)
    insertInto(sqlScript)


def dbSelectType(id, name):
    if id == "0" and name == "0":
        sqlScript = "select * from type"
    elif id == "0":
        sqlScript = "select * from type where name = '{a}'".format(a=name)
    else:
        sqlScript = "select * from type where id_type = '{a}'".format(a=id)
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
    sqlScript = "INSERT INTO alco(id_hash, id_type, name, manufacturer) VALUES('{a}', '{b}', '{c}', '{d}');".format(a=id_hash, b=id_type, c=name, d=manufacturer)
    insertInto(sqlScript)


def dbSelectAlco(id_hash, id_type):
    if id_hash == "0" and id_type == "0":
        sqlScript = "select * from alco "
    elif id_hash == "0":
        sqlScript = "select * from alco where id_type = '{a}'".format(a=id_type)
    else:
        sqlScript = "select * from alco where id_hash = '{a}'".format(a=id_hash)
    return selectFrom(sqlScript)




def dbInsertIngridient(name, description):
    sqlScript = "INSERT INTO ingridient(name, description)VALUES('{a}', '{b}');".format(a=name, b=description)
    insertInto(sqlScript)


def dbSelectIngridient(id_igridient, name):
    if id_igridient == "0" and name == "0":
        sqlScript = "select * from  ingridient"
    elif id_igridient == "0":
        sqlScript = "select * from ingridient where name = '{a}'".format(a=name)
    else:
        sqlScript = "select * from ingridient where id_igridient = '{a}'".format(a=id_igridient)
    return selectFrom(sqlScript)




def dbInsertRecipe(id_usr, title,description, tab_ingridiends, tab_ingridiends_quantity, tab_tools):
    sqlScript = "INSERT INTO recipe(id_usr, title, description, tab_ingridiends, tab_ingridiends_quantity, tab_tools)VALUES ('{a}', '{b}', '{c}',ARRAY{d}, ARRAY{e}, ARRAY{f});".format(a=id_usr, b=title, c=description, d=tab_ingridiends, e=tab_ingridiends_quantity, f=tab_tools)
    insertInto(sqlScript)

def dbSelectRecipe():
    sqlScript = "select * from recipe "
    return selectFrom(sqlScript)


if __name__ == "__main__":

    # dbInsertRecipe(1, "Martini, wstrząśnięte, nie zmieszane",
    #                "100 ml Martini Bianco + plaste cytryny + odrobina skruszonego lodu."
    #                "Połączyć składniki, zamieszać", [3,5,6], [1, 200, 1], [7, 5])

    # dbInsertIngridient(name, description)
    # dbInsertIngridient("Cola", "żródło kofeiny i cukru")
    # dbInsertIngridient("cytrna", "żródło kwasoty")
    # dbInsertIngridient("vodka", " źródło procentów")
    # dbInsertIngridient("martini", "dla smaku")
    # dbInsertIngridient("lód", "dla ochłody")
    # dbInsertIngridient("sok pomarańczony", "dla smaku")
    # dbInsertIngridient("Johny Walker", "źródło procentów i smaku")

    # dbInsertIngridient("sok pożeczkowy", "dla koloru")
    # dbInsertIngridient("sok bananowy", "do smaku")

    # dbInserAlco(id_hash, id_type, name, manufacturer)
    # dbInserAlco(2, 9, 'coca-cola', 'Coca-Cola')
    # dbInserAlco(3, 10, 'cytryna zółta', 'Nature')
    # dbInserAlco(4, 9, 'ice', 'Nature')
    # dbInserAlco(5, 3, 'Martini Bianco', 'babcia')
    # dbInserAlco(6, 11, 'shaker manualny', 'Tłocznia metali')
    # dbInserAlco(7, 9, 'sok porzeczkowy', 'Tymbark')
    # dbInserAlco(8, 12, 'Johny Walker', 'Johny Walker')
    # dbInserAlco(9, 3, 'Carlo Rossi', 'Carlo Rossi')
    # dbInserAlco(10, 6, 'Wyborowa', 'Wyborowa SA')

    # dbInsertType("Non-alkohol")
    # dbInsertType("Owoc")
    # dbInsertType("sprzęt")
    # dbInsertType("Whiskey")

    #2  dbInsertHash('cola.png')
    #3  dbInsertHash('cytryna.png')
    #4  dbInsertHash('lód.png')
    #5  dbInsertHash('martini.png')
    #6  dbInsertHash('shacker.png')
    #7  dbInsertHash('sok.png')
    #8  dbInsertHash('whisky.png')
    #9  dbInsertHash('wino.png')
    #10 dbInsertHash('wodka.png')

    print("\nTYPE !!!!!")
    for elem in dbSelectTool("0"):
        print(elem)

    print("HASH !!!!!")
    for elem in dbSelectHash("0", "0"):
        print(elem)

    print("\nAlco !!!!!")
    for elem in dbSelectAlco("0", "0"):
        print(elem)

    print("\nTYPE !!!!!")
    for elem in dbSelectType("0", "0"):
        print(elem)

    print("\nIngredient !!!!!")
    for elem in dbSelectIngridient("0", "0"):
        print(elem)

    print("\nPrzepisy !!!!!!!!!")
    for elem in dbSelectRecipe():
        print(elem)




