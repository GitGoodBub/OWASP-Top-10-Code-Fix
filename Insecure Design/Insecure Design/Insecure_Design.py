@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    token = request.form['token']
    new_password = request.form['new_password']

    user = User.query.filter_by(email=email).first()
    if not user or not verify_reset_token(email, token):
        abort(403)

    user.password = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=16)
    db.session.commit()
    return 'Password reset successful'