from werkzeug.security import check_password_hash

input_password = request.form['password']
user = User.query.filter_by(username=request.form['username']).first()

if user and check_password_hash(user.password, input_password):
    # Login success
else:
    abort(401)
