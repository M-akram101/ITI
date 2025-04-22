from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from flask import jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "iTi_Zagazig_2025"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)




class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    employees_count = db.Column(db.Integer(), nullable=False)

    def _repr_(self):
        return f"<Company: {self.name}>"
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) 
    hashed_password = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)


# Forms
class CompanyCreationForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    address = StringField("address", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
    employees_count = IntegerField("employees_count", validators=[DataRequired()])
    submit = SubmitField("Create Job")


@app.route("/create/company", methods=["GET", "POST"])
def create_company():
    form = CompanyCreationForm()
    if form.validate_on_submit():
        data = Company(
            name=form.name.data,
            address=form.address.data,
            description=form.description.data,
            employees_count=form.employees_count.data,
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for("get_all_companies"))
    return render_template("create_company.html", form=form)


@app.route("/companies")
def get_all_companies():
    company = Company.query.all()
    return render_template("companies.html", Companies=company)




############

#################CRUD stores
@app.route('/user/stores', methods=['GET'])
def get_all_stores():
    stores = Store.query.all()
    data = [
        {
            'id': store.id,
            'name': store.name,
            'product': store.product,
        } for store in stores
    ]
    return jsonify(data)

@app.route('/user/store/<id>', methods = ['GET'])
@jwt_required()
def get_store(id):
    store = Store.query.get_or_404(id)
    data = {
        'id': store.id,
        'name': store.name,
        'product': store.product
    }
    return jsonify(data)

@app.route("/user/create-store", methods=["POST"])
@jwt_required()

def create_store():
    data = request.get_json()
    new_store = Store(
        name=data['name'],
        product=data['product']
    )
    db.session.add(new_store)
    db.session.commit()
    return jsonify({'message': 'Store created successfully!'}), 201

@app.route('/user/update-store/<id>', methods=['PUT'])
@jwt_required()

def update_store(id):
    data = request.get_json()
    store = Store.query.get_or_404(id)
    
    store.name = data['name']
    store.product = data['product']
    
    db.session.commit()
    
    return jsonify({"message": "Store Updated Successfully!"}), 201

@app.route('/user/delete-store/<id>', methods=['DELETE'])
@jwt_required()

def delete_store(id):
    store = Store.query.get_or_404(id)
    db.session.delete(store)
    db.session.commit()
    return jsonify({"message": "Store Deleted Successfully!"}), 200
   

##############



@app.route('/api/auth/register', methods = ['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username= data['username']).first():
        return jsonify({"message": "Username Already Exists"}), 400
    
    user = User(username = data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "User Created Successfully!"}), 201


@app.route("/api/auth/login", methods=['POST'])
def login():
    data = request.get_json()
    
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        token = create_access_token(identity=str(user.id))
        
        return jsonify({"access_token": token}), 200
    
    return jsonify({"message": "invalid credentials"}), 401
        
@app.route('/api/profile', methods= ['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    
    user = User.query.get(int(user_id))
    
    return jsonify(
        {
            "id": user.id,
            "username": user.username
        }
    )

"""
create a company route that display all companies
- company name
- company address
- company description
- company employees count 
"""

# Company = [
#     {
#         "name": "DELL",
#         "location": "Cairo",
#         "description": "Software company",
#         "employees_count": 2000,
#     },
#     {
#         "name": "Microsoft",
#         "location": "Giza",
#         "description": "Software company",
#         "employees_count": 1000,
#     },
#     {
#         "name": "Google",
#         "location": "Alexandria",
#         "description": "Software company",
#         "employees_count": 500,
#     },
#     {
#         "name": "Apple",
#         "location": "Cairo",
#         "description": "Software company",
#         "employees_count": 100,
#     },
# ]
# LAB 1
"""
create a company route that display all companies
- company name
- company location
- company description
- company employees count
"""


# LAB 2:
"""
1.  Create Table for company:
    - id (primary key)
    - name
    - description
    - employees_count
    - location
2. create View-all and view-single and Create apis for the company
3. use flask forms to create the company
"""

# LAB 3
"""
1.⁠ ⁠Create CRUD Operations Apis For Company
2.⁠ ⁠make sure that only registerd users can do Create And Update And Delete on Company APIs
"""