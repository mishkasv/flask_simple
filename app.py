import random
from flask import Flask, url_for
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password,current_user
from flask_security.models import fsqla_v2 as fsqla
from flask_admin import helpers as admin_helpers
import config
import datetime

from admin.view import MyModelView, MyAdminIndexView, MyModelViewAdress, ExtendedLoginForm

db = SQLAlchemy()
fsqla.FsModels.set_db_info(db)
app = Flask(__name__)
migrate = Migrate(app, db)

app.config.from_object("config.Config")
admin = Admin(app,index_view=MyAdminIndexView(), name=config.Config.CATALOG_TITLE, base_template = 'my_master.html', template_mode='bootstrap3')

db.init_app(app)

with app.app_context():
    import routes.catalog
    from models.models import Product, Address, User,Role
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Product, db.session))
    admin.add_view(MyModelViewAdress(Address, db.session))

    user_datastore = SQLAlchemyUserDatastore(db, User,Role)
    security = Security(app, user_datastore, login_form=ExtendedLoginForm)

    db.create_all()
    if not user_datastore.find_user(email="test@me.com",username='test'):
        user_datastore.create_user(username= 'test',email="test@me.com", password=hash_password("password"), created = datetime.datetime.now())
        user_datastore.create_role(name='superuser')
        user_datastore.add_role_to_user(User.query.filter_by(username='test').first(),Role.query.filter_by(name='superuser').first())

    # def create_sampe_database():
    if not Product.query.filter_by(name='name1'):
        for i in range(10):
            prod = Product(name=f'name{i}',color=f'color{i}',weight=i**2,price=i**2,numbers=1)
            addr = Address(product=prod,country=f'country{i}',city=f'city{i}',street=f'street{i}',number_of_building=random.randint(1,10))
            db.session.add(prod)
            db.session.add(addr)
    db.session.commit()





    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
        )

if __name__ == '__main__':
    app.run(debug=True)
