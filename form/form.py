# from flask import Flask, render_template
# app = Flask(__name__)
#
# @app.route('/showid/<id>')
# def user(id):
# 	return render_template('user.html', id=id)
#
# if __name__ == '__main__':
# 	app.run(debug=True)
# # from app import app
# # @app.route('/showid/<id>')
# # def index(id):
# #     return 'my id is'+id


from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/showid/1846cse00685')
def success(id):
   return 'My id is %s' % id

@app.route('/view',methods = ['POST', 'GET'])
def view():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',id = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',id = user))

if __name__ == '__main__':
   app.run(debug = True)