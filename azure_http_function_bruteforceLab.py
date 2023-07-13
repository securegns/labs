import logging
import azure.functions as func

HTML_LOGIN_PAGE = '<!DOCTYPE html><html><head><title>Login Page</title><style>body{font-family:Arial,sans-serif;background-color:#f2f2f2;}.container{max-width:400px;margin:0 auto;padding:20px;background-color:#ffffff;border-radius:5px;box-shadow:0 0 10px rgba(0,0,0,.1);}.container h2{text-align:center;margin-bottom:20px;}.form-group{margin-bottom:15px;}.form-group label{display:block;font-weight:bold;margin-bottom:5px;}.form-group input{width:100%;padding:8px;border-radius:3px;border:1px solid #ccc;}.form-group button{width:100%;padding:8px;background-color:#4CAF50;border:none;color:#fff;cursor:pointer;border-radius:3px;}</style><script>function submitForm(){var e=document.getElementById("username").value,t=document.getElementById("password").value;fetch("",{method:"POST",body:new FormData().append("username",e).append("password",t)}).then(function(e){e.ok?console.log("Login successful"):console.log("Login failed")}).catch(function(e){console.log("Error:",e)})}</script></head><body><div class="container"><h2>Login</h2><div class="form-group"><label for="username">Username:</label><input type="text" id="username" name="username" required></div><div class="form-group"><label for="password">Password:</label><input type="password" id="password" name="password" required></div><div class="form-group"><button onclick="submitForm()">Login</button></div></div></body></html>'
HTML_LOGIN_FAILED = '<!DOCTYPE html><html><head><title>Login Failed</title><style>body{font-family:Arial,sans-serif;background-color:#f2f2f2;}.container{max-width:400px;margin:0 auto;padding:20px;background-color:#ffffff;border-radius:5px;box-shadow:0 0 10px rgba(0,0,0,.1);}.container h2{text-align:center;margin-bottom:20px;}.error-message{color:red;text-align:center;font-weight:bold;}</style></head><body><div class="container"><h2>Login Failed</h2><p class="error-message">Invalid username or password.</p></div></body></html>'
HTML_LOGIN_SUCESS = '<!DOCTYPE html><html><head><title>Welcome</title><style>body{font-family:Arial,sans-serif;background-color:#f2f2f2;}.container{max-width:400px;margin:0 auto;padding:20px;background-color:#ffffff;border-radius:5px;box-shadow:0 0 10px rgba(0,0,0,.1);}.container h2{text-align:center;margin-bottom:20px;}.success-message{color:green;text-align:center;font-weight:bold;}</style></head><body><div class="container"><h2>Login Successful</h2><p class="success-message">Hello admin</p></div></body></html>'


def main(req: func.HttpRequest) -> func.HttpResponse:
    # if GET
    if func.method == "GET":
        html_content =  HTML_LOGIN_PAGE
    # if POST
    if func.method == "POST":
        req_body = req.get_json()
        username = req_body.get('username')
        password = req_body.get('password')
        if username == "admin" && password == "Password@123":
            html_content =  HTML_LOGIN_SUCESS
        else:
            html_content =  HTML_LOGIN_FAILED

    headers = {
        'Content-Type': 'text/html'
    }

    # Return the HTML page as the response
    return func.HttpResponse(html_content, headers=headers)
