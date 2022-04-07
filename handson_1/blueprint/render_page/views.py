from flask import Blueprint,render_template,request

page = Blueprint('render_page',__name__,template_folder='templates')


@page.route('/page_one')
def page_one():
    text = request.args.get('text')
    return render_template('page/render_nidhin_content.html',text=text)



@page.route('/page_two')
def page_two():
    text = request.args.get('text')
    return render_template('page/render_vishnu_content.html',text=text)
