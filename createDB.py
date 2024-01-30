import sqlite3

connection = sqlite3.connect("restaurant.db")
cursor = connection.cursor()


try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT NOT NULL,
            name TEXT,
            extra_info TEXT
        )
    ''')
    print("Table created successfully.")
except sqlite3.Error as e:
    print("Error creating table:", e)


try:
    cursor.execute("INSERT INTO users (username, password, user_type, name, extra_info) VALUES ('Mkunafi', '123456789', 'Server', 'Marwa Kunafi', 'Kind Fast Service')")
    cursor.execute("INSERT INTO users (username, password, user_type, name, extra_info) VALUES ('Wchrad', 'recep', 'Reception', 'Zinab Cherad', 'Polite and Kind')")
    cursor.execute("INSERT INTO users (username, password, user_type, name, extra_info) VALUES ('Jloukili', '123456789', 'Server', 'Jad Loukili', 'Elegant Fast Service and Kind')")
    cursor.execute("INSERT INTO users (username, password, user_type, name, extra_info) VALUES ('Otaraki', 'chef123', 'Chef', 'Omar Taraki', 'Best Chef in Our Restaurant')")
    cursor.execute("INSERT INTO users (username, password, user_type, name, extra_info) VALUES ('Ntarik', '1234', 'Reception', 'Nayrouz Tarik', 'The most strict Receptionist')")
    connection.commit()
    print("Sample data inserted successfully.")
except sqlite3.Error as e:
    print("Error inserting sample data:", e)

connection.close()

print("Database, table, and sample data created successfully.")
