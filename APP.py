from flask import Flask, render_template

app = Flask(__name__,template_folder='Template',static_folder='Static')

@app.route('/')
def login():
    return render_template(r'teste.html')


if __name__ == '__main__':
    app.run(debug=True)