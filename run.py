from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

if __name__ == '__main__':
    app = create_app()
    manager = Manager(app)

    @manager.command
    def run():
        app.run(debug=True, host='0.0.0.0')

    manager.add_command('db', MigrateCommand)
    manager.run()
