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

HTML_OTP_PAGE = """
<html>
<head>
    <title>OTP Page</title>
</head>
<body>
    <form method="POST">
        OTP: <input type="text" name="otp"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

HTML_OTP_FAILED = """
<html>
<head>
    <title>OTP Page</title>
</head>
<body>
    <form method="POST">
        OTP: <input type="text" name="otp"><br>
        <input type="submit" value="Submit">
    </form>
    <p>OTP is wrong. Please try again.</p>
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
OTP = "1234"

def main(req: func.HttpRequest) -> func.HttpResponse:
    method = req.method.upper()

    # if GET
    if method == "GET":
        html_content = HTML_LOGIN_PAGE
    # if POST
    elif method == "POST":
        username = req.form.get('username')
        password = req.form.get('password')
        otp = req.form.get('otp')
        if username == "admin" and password == "Password@123" and otp is None:
            html_content = HTML_OTP_PAGE
        elif otp == OTP:
            html_content = HTML_LOGIN_SUCCESS
        elif otp is not None and otp != OTP:
            html_content = HTML_OTP_FAILED
        else:
            html_content = HTML_LOGIN_FAILED

    headers = {
        'Content-Type': 'text/html'
    }

    # Return the HTML page as the response
    return func.HttpResponse(html_content, headers=headers)
