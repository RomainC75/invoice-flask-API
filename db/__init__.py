from dotenv import dotenv_values
import pymysql
config = dotenv_values(".env")
print(config)

conn = pymysql.connect(
    host = config['DB_HOST'],
    port = int(config['DB_PORT']),
    user = config['DB_USER'],
    password = config['DB_PASS'],
    db = config['DB_NAME']
)
cursor = conn.cursor()

create_table="""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        firstname VARCHAR(100),
        lastname VARCHAR(100),
        createdAt Date,
        updatedAt Date
);
"""
cursor.execute(create_table)
