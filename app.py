from flask import Flask, render_template, make_response, redirect, request

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route('/')
def index():
    theme = request.cookies.get('theme', 'dark')  # tema padrão é dark
    return render_template('index.html', theme=theme)

@app.route('/toggle-theme')
def toggle_theme():
    response = make_response(redirect('/'))
    current_theme = request.cookies.get('theme', 'dark')
    new_theme = 'light' if current_theme == 'dark' else 'dark'
    response.set_cookie('theme', new_theme)
    return response

if __name__ == "__main__":
    app.run(debug=True)
