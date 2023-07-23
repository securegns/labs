import azure.functions as func
import subprocess

HTML_TEMPLATE = """
<html>
    <head>
        <title>HTTP Header Lookup</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="p-3">
        <h1>Check HTTP Headers for a URL</h1>
        <form method="POST">
            <input type="text" class="form-control" name="url" required placeholder="Enter a URL">
            <input type="submit" class="btn btn-primary mt-2" value="Check">
        </form>
        <br/>
        <pre>{results}</pre>
    </body>
</html>
"""

def get_headers(url):
    """Send a request to the given URL and return the headers."""
    command = f'curl -I {url}'
    try:
        result = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        return "Curl command failed with error: " + str(e)
    return result

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = req.form.get("url")

    if req.method == "POST" and url:
        results = get_headers(url)
    else:
        results = ""

    html_content = HTML_TEMPLATE.format(results=results)
    headers = {"Content-Type": "text/html"}
    return func.HttpResponse(html_content, headers=headers)
