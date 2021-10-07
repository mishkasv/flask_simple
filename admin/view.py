from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import current_user

class MyAdminIndexView(AdminIndexView):
    pass

class MyModelView(ModelView):
    column_display_all_relations = True
    page_size = 50  # the number of entries to display on the list view
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
                )

class MyModelViewAdress(ModelView):
    column_display_all_relations = True
    page_size = 50  # the number of entries to display on the list view
    column_filters = ['country','street','city']
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
                )

from flask_security.forms import LoginForm
from wtforms import StringField
from wtforms.validators import InputRequired

class ExtendedLoginForm(LoginForm):
    email = StringField('Username or Email Address', [InputRequired()])