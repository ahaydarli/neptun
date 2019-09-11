from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(use_reloader=True, debug=True)


if __name__ == "__main__":
    manager.run()
