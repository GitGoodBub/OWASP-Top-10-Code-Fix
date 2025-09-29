from flask_login import login_required, current_user
from flask import abort

@app.route('/account/<user_id>')
@login_required
def get_account(user_id):
    if current_user.id != int(user_id) and not current_user.is_admin:
        abort(403)
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())