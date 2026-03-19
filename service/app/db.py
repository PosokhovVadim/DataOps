import psycopg2

def log_to_db(x, y, latency):
    conn = psycopg2.connect(
        dbname="ml",
        user="ml",
        password="ml",
        host="db"
    )
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO logs (input, output, latency) VALUES (%s, %s, %s)",
        (x, y, latency)
    )

    conn.commit()
    conn.close()