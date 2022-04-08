   
from flask import Flask,render_template
from flask_mail import Mail, Message

app =Flask(__name__,template_folder='templates')
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nidhinkumar710@gmail.com'
app.config['MAIL_PASSWORD'] = 'nidhinkumar123'
app.config['MAIL_DEFAULT_SENDER'] = 'nidhinkumar710@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', recipients = ['nidhin@proaibots.com'])
   msg.html = render_template('email.html')
   mail.send(msg)
   return "Mail Sent Successfully"

if __name__ == '__main__':
   app.run(debug = True)