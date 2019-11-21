from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from project.apps import create_app,db

app = create_app('config')
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)


@app.route('/')
def index():
    return 'index'


# if __name__ == '__main__':
#     app.run(host='192.168.179.131')