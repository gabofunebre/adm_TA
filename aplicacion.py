from flask import Flask, render_template, request, redirect, url_for, session
from base_de_datos import validar_credenciales

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Establece una clave secreta para la sesión Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    password = request.form['password']

    if validar_credenciales(usuario, password):
        # Autenticación exitosa, guardar datos en la sesión
        session['username'] = usuario

        # Redirigir a la página del dashboard
        return redirect(url_for('dashboard'))
    else:
        # Autenticación fallida, mostrar mensaje de error
        return render_template('index.html', error='Usuario o contraseña inválida')

@app.route('/dashboard')
def dashboard():
    # Verificar si el usuario está autenticado
    if 'username' in session:
        # El usuario está autenticado, mostrar datos del usuario
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        # El usuario no está autenticado, redirigir al inicio de sesión
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Limpiar todos los datos de la sesión al cerrar sesión
    session.clear()
    return redirect(url_for('index'))


@app.route('/register')
def register():
    # Lógica para el registro de usuarios
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
