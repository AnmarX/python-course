import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Sample data for students and courses
students = [
    'John Smith',
    'Jane Doe',
    'Michael Johnson'
]

courses = [
    'Mathematics',
    'Physics',
    'Chemistry'
]

# Insert students into the Student table
for student in students:
    cur.execute("INSERT INTO student (name) VALUES (%s) RETURNING student_id", (student,))
    student_id = cur.fetchone()[0]  # Retrieve the generated student_id
    conn.commit()  # Commit the changes

    # Insert enrollment records for each student and course combination
    for course in courses:
        cur.execute("INSERT INTO course (title) VALUES (%s) RETURNING course_id", (course,))
        course_id = cur.fetchone()[0]  # Retrieve the generated course_id
        conn.commit()  # Commit the changes

        cur.execute("INSERT INTO enrollment (student_id, course_id) VALUES (%s, %s)", (student_id, course_id))
        conn.commit()  # Commit the changes

# Close the cursor and database connection
cur.close()
conn.close()
