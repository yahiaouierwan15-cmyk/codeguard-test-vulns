"""
SQL Injection — intentionally vulnerable (CodeGuard AI test fixture)
DO NOT USE IN PRODUCTION
"""
import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULN CWE-89: string concatenation in SQL
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchone()

def get_orders(user_id):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    # VULN CWE-89: f-string in SQL
    cursor.execute(f"SELECT * FROM orders WHERE user_id = {user_id}")
    return cursor.fetchall()

def search_products(term):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    # VULN CWE-89: % formatting
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (term,))
    return cursor.fetchall()

def admin_delete(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULN CWE-89: concatenation with DELETE
    cursor.execute("DELETE FROM users WHERE id = " + str(user_id))
    conn.commit()