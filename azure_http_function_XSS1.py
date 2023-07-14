import azure.functions as func

HTML_TEMPLATE = """
<html>
    <head>
        <title>Library Search System</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="p-3">
        <h1>Search for a Book or Author</h1>
        <form method="POST">
            <input type="text" class="form-control" name="query" required placeholder="Enter book or author name">
            <input type="submit" class="btn btn-primary mt-2" value="Search">
        </form>
        <br/>
        {results}
    </body>
</html>
"""

# A simple dictionary representing our "database"
DATABASE = {
    "Author1": ["Book1", "Book2"],
    "Author2": ["Book3", "Book4"],
}

def search(query):
    """Search for the query in the database and return HTML table of results."""
    table_rows = ""
    for author, books in DATABASE.items():
        if query.lower() in author.lower() or any(query.lower() in book.lower() for book in books):
            for book in books:
                table_rows += f"<tr><td>{author}</td><td>{book}</td></tr>"
    if table_rows:
        return f"<h2>Results for '{query}'</h2><table class='table'><thead><tr><th>Author</th><th>Book</th></tr></thead><tbody>{table_rows}</tbody></table>"
    else:
        return f"<h2>No results found for '{query}'</h2>"

def main(req: func.HttpRequest) -> func.HttpResponse:
    query = req.form.get("query")
    if query:
        results = search(query)
    else:
        results = ""
    html_content = HTML_TEMPLATE.format(results=results)
    headers = {"Content-Type": "text/html"}
    return func.HttpResponse(html_content, headers=headers)
