from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Crud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(120))

@app.route('/')
def indexpage():
    crud=Crud.query.all()
    return render_template('index.html', crud=crud)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=='POST':
        crud=Crud(
            name=request.form['name'],
            surname=request.form['surname']
        )
        db.session.add(crud)
        db.session.commit()
        return redirect('/')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

