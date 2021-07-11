from datetime import datetime
from flask import Flask,render_template,url_for,session,redirect,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

web_form = Flask(__name__)
bootstrap = Bootstrap(web_form)
moment = Moment(web_form)
# 配置FLask-WTF
web_form.config['SECRET_KEY'] = 'hard to guess string'

# 没有methods,该视图就只注册为GET请求
@web_form.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you hava changed your name!')
        # name = form.name.data
        # form.name.data =''
        session['name'] = form.name.data
        return redirect(url_for('index'))
    # return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())
    return render_template('index.html', form=form, name=session.get('name'))

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    web_form.run()