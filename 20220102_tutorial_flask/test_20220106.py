from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
import secrets

a = secrets.token_hex(16)

app = Flask(__name__)
app.config["SECRET_KEY"] = '93bed4da8519f59f24d13fe909ebb2d3'


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger)
        flash(f'{form.username.data} 님 가입 완료!', 'success')
        return redirect(url_for('home'))
    return render_template('register2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
