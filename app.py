from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods = ["POST"])
def search():
    data = request.form
    school = data["school"]
    department = data["department"]

    import sqlite3
    conn = sqlite3.connect("schools.db")
    
    command = """
    SELECT sch.Name, s.Name, s.Department, s.Contact, sch.Address
    FROM SCHOOL sch, STAFF s
    WHERE sch.Name LIKE ? AND s.Department = ? AND sch.SchoolCode = s.SchoolCode
    """
    
    cursor = conn.execute(command,("%" + school + "%", department)).fetchall()    
    conn.commit()
    conn.close()
    
    return render_template("results.html", cursor = cursor)

if __name__ == "__main__":
    app.run(debug=True) #port = 5000
