from flask import Flask, render_template, request, redirect, url_for
from peewee import *

# Initialize Flask app
app = Flask(__name__)

# Define database connection
database = SqliteDatabase('boe_spending.db')

# Define base model for Peewee
class BaseModel(Model):
    class Meta:
        database = database

# Define Vendors model
class Vendors(BaseModel):
    # Define fields
    agency_name = TextField(null=True)
    amount = FloatField(null=True)
    exclude = TextField(null=True)
    fiscal_year = TextField(null=True)
    payee_name = TextField(null=True)
    payee_zip = TextField(null=True)
    purpose_of_payment_baltimore_county_only = TextField(null=True)
    slug = TextField(null=True)

    class Meta:
        table_name = 'vendors'
        # Indicate that there is no primary key in this table
        primary_key = False

# Define Jurisdiction model
class Jurisdiction(BaseModel):
    # Define fields
    agency_name = TextField(null=True)
    slug = TextField(null=True)
    total_records = IntegerField(default=0)
    total_amount = FloatField(default=0.0)

    class Meta:
        table_name = 'jurisdictions'
        # Indicate that there is no primary key in this table
        primary_key = False

# Route for homepage
@app.route("/")
def index():
    # Retrieve all jurisdictions and order them by agency name
    jurisdictions = Jurisdiction.select().order_by(Jurisdiction.agency_name)
    return render_template('index.html', jurisdictions=jurisdictions)

# Route for search form submission
@app.route("/search", methods=['POST'])
def search():
    # Get search term from form
    search_term = request.form.get('search_term')
    # Search for vendors containing the search term in payee name and order by amount
    results = Vendors.select().where(Vendors.payee_name.contains(search_term)).order_by(Vendors.amount.desc())
    return render_template('index.html', results=results)

# Route for handling form submission and redirection to jurisdiction page
@app.route("/redirect", methods=["POST"])
def redirect_to_jurisdiction():
    # Get slug from form
    slug = request.form.get("slug")
    # Redirect to jurisdiction page with slug parameter
    return redirect(url_for("jurisdiction", slug=slug))

# Route for displaying jurisdiction details
@app.route("/jurisdiction/<slug>")
def jurisdiction(slug):
    # Get jurisdiction details based on slug
    jurisdiction = Jurisdiction.get(Jurisdiction.slug == slug)
    # Retrieve associated vendor records and order by amount
    associated_vendors = Vendors.select().where(Vendors.agency_name == jurisdiction.agency_name).order_by(Vendors.amount.desc())
    return render_template('jurisdiction.html', jurisdiction=jurisdiction, vendors=associated_vendors)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
