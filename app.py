from flask import Flask, render_template, request, redirect, url_for
from peewee import *

app = Flask(__name__)
database = SqliteDatabase('boe_spending.db')

class BaseModel(Model):
    class Meta:
        database = database

class Vendors(BaseModel):
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
        primary_key = False

class Jurisdiction(BaseModel):
    agency_name = TextField(null=True)
    slug = TextField(null=True)
    total_records = IntegerField(default=0)
    total_amount = FloatField(default=0.0)

    class Meta:
        table_name = 'jurisdictions'
        primary_key = False

@app.route("/")
def index():
    jurisdictions = Jurisdiction.select().order_by(Jurisdiction.agency_name)
    return render_template('index.html', jurisdictions=jurisdictions)

@app.route("/search", methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    results = Vendors.select().where(Vendors.payee_name.contains(search_term)).order_by(Vendors.amount.desc())
    return render_template('index.html', results=results)

@app.route("/redirect", methods=["POST"])
def redirect_to_jurisdiction():
    slug = request.form.get("slug")
    return redirect(url_for("jurisdiction", slug=slug))

@app.route("/jurisdiction/<slug>")
def jurisdiction(slug):
    jurisdiction = Jurisdiction.get(Jurisdiction.slug == slug)
    # Retrieve associated records from Vendors table
    associated_vendors = Vendors.select().where(Vendors.agency_name == jurisdiction.agency_name).order_by(Vendors.amount.desc())
    return render_template('jurisdiction.html', jurisdiction=jurisdiction, vendors=associated_vendors)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
