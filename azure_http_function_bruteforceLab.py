HTML_LOGIN_PAGE = """
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

HTML_LOGIN_FAILED = """
<html>
<head>
    <title>Login Failed</title>
</head>
<body>
    <h1>Login Failed</h1>
    <p>Incorrect username or password. Please try again.</p>
</body>
</html>
"""

HTML_LOGIN_SUCCESS = """
<html>
<head>
    <title>Login Success</title>
</head>
<body>
    <h1>Login Successful</h1>
    <p>Welcome, admin!</p>
</body>
</html>
"""

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    method = req.method.upper()

    # if GET
    if method == "GET":
        html_content = HTML_LOGIN_PAGE
    # if POST
    elif method == "POST":
        username = req.form.get('username')
        password = req.form.get('password')
        if username == "admin" and password == "Password@123":
            html_content = HTML_LOGIN_SUCCESS
        else:
            html_content = HTML_LOGIN_FAILED

    headers = {
        'Content-Type': 'text/html'
    }

    # Return the HTML page as the response
    return func.HttpResponse(html_content, headers=headers)
