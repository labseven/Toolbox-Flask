from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)
try:
    text_wall = pickle.load(open("wall.p", "rb"))
except:
    text_wall = []

@app.route('/')
@app.route('/page/<name>')
def main_page(name=None):
    return render_template('wall_page.html', text_wall=text_wall, name=name)

@app.route('/add_text', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        add_text_to_page(request.form['in_text'])
        return redirect('/')
    else:
        return show_add_text_form()

def add_text_to_page(in_text):
    text_wall.append(in_text)
    pickle.dump(text_wall, open("wall.p", "wb"))

def show_add_text_form():
    return render_template('add_text.html')

if __name__ == '__main__':
    app.run(debug=True)
