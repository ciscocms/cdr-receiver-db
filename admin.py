from receiver import app
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from models import Record, RecordAdmin

admin = Admin(app, name='cdr-admin', template_mode='bootstrap3')
admin.add_view(RecordAdmin(Record))
app.config['SECRET_KEY'] = '9fc7c7b34f02403e85b432ab918e6571'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8444)
