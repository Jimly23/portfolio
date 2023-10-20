import mysql.connector, random, string



def inputUser(username,email,password):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Hardiansyah_23",
        database = "portfolio"
    )
    cursor = db.cursor()

    # Membuat id user
    panjang_string = 3
    id_str = ''.join(random.choice(string.ascii_uppercase) for _ in range(panjang_string))
    id_angka = random.randint(100,999)
    id_user = f'{id_str}{str(id_angka)}'

    # Insert data ke database
    insert = "INSERT INTO users(id,username,email,password) VALUES(%s,%s,%s,%s)"
    values = (id_user,username,email,password)
    cursor.execute(insert,values)
    
    db.commit()
    cursor.close()

def show_users():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Hardiansyah_23",
        database = "portfolio"
    )
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    

    return users


# print(show_users())