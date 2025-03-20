import streamlit as st
import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="mydb",
    user="admin",
    password="adminpassword",
    host="my_postgres",  # Use PostgreSQL container name as hostname
    port="5432"
)
cur = conn.cursor()

# Example query
cur.execute("SELECT version();")
db_version = cur.fetchone()

st.title("Streamlit App with PostgreSQL")
st.write("Connected to database:", db_version)

cur.close()
conn.close()
