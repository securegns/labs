import os
import azure.functions as func

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <title>Simple Blog</title>
  </head>
  <body>
    <div class="container">
        <div class="row mt-5">
            <div class="col-12">
                <h1 class="text-center">Simple Blog</h1>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-6">
                <h3>Story 1</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus.</p>
                <img src="/api/blog?file_name=story1.jpg" class="img-fluid" alt="Story 1 Image">
            </div>
            <div class="col-6">
                <h3>Story 2</h3>
                <p>Sed euismod nisi porta lorem mollis aliquam. Ut euismod, turpis sollicitudin lobortis pellentesque.</p>
                <img src="/api/blog?file_name=story2.jpg" class="img-fluid" alt="Story 2 Image">
            </div>
        </div>
    </div>
  </body>
</html>
"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        file_name = req.params.get("file_name")
        if file_name:
            with open(file_name, 'rb') as f:
                file_bytes = f.read()
                return func.HttpResponse(file_bytes, status_code=200)
        else:
            html_content = HTML_TEMPLATE
            headers = {"Content-Type": "text/html"}
            return func.HttpResponse(html_content, headers=headers, status_code=200)

    else:
        return func.HttpResponse("Method not supported", status_code=405)
