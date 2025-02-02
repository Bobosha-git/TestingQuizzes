import sqlite3


con = sqlite3.connect("bot\db\my_database.db")
cur = con.cursor()

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS db_tg (
#             id INTEGER PRIMARY KEY,
#             user_name TEXT,
#             id_tg INTEGER,
# 	        solved_test TEXT,
# 	        count_tests	INTEGER,
# 	        user_answer	INTEGER,
# 	        results1 INTEGER,
# 	        results2 INTEGER,
# 	        results3 INTEGER
#             ) 
#             """)

# cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_id_tg ON db_tg(id_tg);")

# cur.execute("ALTER TABLE db_tg DROP COLUMN results2")

# cur.execute("ALTER TABLE db_tg RENAME COLUMN user_answer TO user_answer TEXT")

# con.commit()
# con.close()

def db_table_val(id_tg: int, user_name: str):
    cur.execute("INSERT OR IGNORE INTO db_tg (id_tg, user_name) VALUES (?, ?)", (id_tg, user_name))
    con.commit()

def db_add_solved_test(solved_test: str, id_tg: int):
    cur.execute("""
        INSERT INTO db_tg (id_tg, solved_test) 
        VALUES (?, ?)
        ON CONFLICT(id_tg) DO UPDATE SET 
        solved_test = excluded.solved_test
    """, (id_tg, solved_test))
    con.commit()

def db_add_user_answer(user_answer: int, id_tg: int):
    cur.execute("SELECT user_answer FROM db_tg WHERE id_tg = ?", (id_tg,))
    row = cur.fetchone()

    if row:
        updated_answer = f"{row[0]},{user_answer}" if row[0] else str(user_answer)
        cur.execute("UPDATE db_tg SET user_answer = ? WHERE id_tg = ?", (updated_answer, id_tg))
    else:
        cur.execute("INSERT INTO db_tg (id_tg, user_answer) VALUES (?, ?)", (id_tg, str(user_answer)))

    con.commit()

def clear_user_answers(id_tg: int):
    cur.execute("UPDATE db_tg SET user_answer = NULL WHERE id_tg = ?", (id_tg,))
    con.commit()

def increment_test_count(id_tg: int):
    cur.execute("SELECT count_tests FROM db_tg WHERE id_tg = ?", (id_tg,))
    row = cur.fetchone()

    if row:
        new_count = row[0] + 1 if row[0] is not None else 1 
        cur.execute("UPDATE db_tg SET count_tests = ? WHERE id_tg = ?", (new_count, id_tg))
    else:
        cur.execute("INSERT INTO db_tg (id_tg, user_answer, count_tests) VALUES (?, ?, ?)", (id_tg, "", 1))

    con.commit()