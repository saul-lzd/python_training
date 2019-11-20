from flask import Flask, redirect, url_for

def create_app():

    app = Flask(__name__, instance_relative_config=True)

    from . import module_1
    app.register_blueprint(module_1.m1)

    from . import module_2
    app.register_blueprint(module_2.m2)

    app.add_url_rule('/p', endpoint='module2.special')

    def wel():
        return 'Welcome to flask again'
    app.add_url_rule('/a', 'mask', wel)

    @app.route('/b')
    def fun_b():
        return redirect(url_for('mask'))

    @app.route('/c')
    def fun_c():
        return redirect(url_for('module1.hello'))

    @app.route('/d')
    def fun_d():
        return redirect(url_for('module2.hello'))

    @app.route('/e')
    def fun_e():
        return redirect(url_for('module2.welcome'))

    print(app.url_map)

    return app
