import azure.functions as func

# Assuming this is our simple database
DB = {
    "J.K. Rowling": ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"],
    "J.R.R. Tolkien": ["The Hobbit", "The Lord of the Rings"],
    "George Orwell": ["1984", "Animal Farm"]
}

HTML_PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">

    <title>Book Search</title>
  </head>
  <body>
    <div class="container">
      <h1>Search for a book or author</h1>
      <form method="POST">
        <div class="form-group">
          <input type="text" class="form-control" name="query" placeholder="Enter book title or author">
        </div>
        <button type="submit" class="btn btn-primary">Search</button>
      </form>
      <br>
      {results}
    </div>
  </body>
</html>
"""

def search_db(query):
    results = []
    for author, books in DB.items():
        if query.lower() in author.lower():
            results.append((author, books))
        else:
            for book in books:
                if query.lower() in book.lower():
                    results.append((author, [book]))
    return results

def generate_results_html(results):
    if not results:
        return "<p>No results found</p>"
    html = '<table class="table"><thead><tr><th scope="col">Author</th><th scope="col">Books</th></tr></thead><tbody>'
    for author, books in results:
        html += f'<tr><td>{author}</td><td>{"<br>".join(books)}</td></tr>'
    html += "</tbody></table>"
    return html

def main(req: func.HttpRequest) -> func.HttpResponse:
    query = req.form.get('query')
    results = ""
    if query:
        search_results = search_db(query)
        results = generate_results_html(search_results)
    html_content = HTML_PAGE.format(results=results)

    headers = {
        'Content-Type': 'text/html'
    }
    return func.HttpResponse(html_content, headers=headers)
