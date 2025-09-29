@app.route('/')
def index():
    return '''
    <html>
      <head>
        <script src="https://cdn.example.com/lib.js"
                integrity="sha384-abc123..."
                crossorigin="anonymous"></script>
      </head>
      <body>Secure Page</body>
    </html>
    '''
