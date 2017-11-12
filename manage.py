from app import app, db
# from flask_script import Manager
# from flask import Flask
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
# @app.cli.command()
# def migratedb():
#     MigrateCommand
# manager = Manager(app)
# Manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()