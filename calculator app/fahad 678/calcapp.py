from flask import Flask, redirect, render_template,request
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = '7rwtzhl0tkg9obj9'



@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        
        elif operation == 'mod':
            sum = float(num1) % float(num2)
            return render_template('app.html', sum=sum)


        else:
            return render_template('app.html')




if __name__ == '__main__':
    app.run(debug=True)

