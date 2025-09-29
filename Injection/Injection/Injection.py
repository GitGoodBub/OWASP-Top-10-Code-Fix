username = request.args.get('username')
user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()