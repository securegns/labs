import sqlite3
import azure.functions as func

# HTML template for the login page
HTML_LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-3">
    <form method="POST">
        Username: <input type="text" class="form-control" name="username"><br>
        Password: <input type="password" class="form-control" name="password"><br>
        <input type="submit" class="btn btn-primary mt-2" value="Submit">
    </form>
</body>
</html>
"""

# HTML template for the response
HTML_RESPONSE = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Result</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-3">
    <h1>{}</h1>
</body>
</html>
"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Initialize SQLite in-memory database and create users table
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (username text, password text)')
    cursor.execute("INSERT INTO users VALUES ('admin', 'password123')")
    conn.commit()

    if req.method == 'POST':
        username = req.form.get('username')
        password = req.form.get('password')

        # Find user in the database
        cursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        user = cursor.fetchone()

        if user:
            html_content = HTML_RESPONSE.format('Welcome admin!')
        else:
            html_content = HTML_RESPONSE.format('Wrong credentials.')

        headers = {'Content-Type': 'text/html'}
        return func.HttpResponse(html_content, headers=headers)

    else:  # GET request
        headers = {'Content-Type': 'text/html'}
        return func.HttpResponse(HTML_LOGIN_PAGE, headers=headers)
