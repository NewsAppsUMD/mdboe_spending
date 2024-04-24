from peewee import *

# Connect to the existing database
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

# Define the model for the new table with a sequential id column
class VendorsWithID(Model):
    id = AutoField()  # This will be a new auto-increment primary key column
    agency_name = TextField(null=True)
    amount = FloatField(null=True)
    exclude = TextField(null=True)
    fiscal_year = TextField(null=True)
    payee_name = TextField(null=True)
    payee_zip = TextField(null=True)
    purpose_of_payment_baltimore_county_only = TextField(null=True)
    slug = TextField(null=True)

    class Meta:
        database = database
        table_name = 'vendors_new'  # New table name

# Define a migration function
def migrate_to_new_table():
    # Create the new table
    with database.atomic():
        database.create_tables([VendorsWithID])

        # Migrate data from old table to new table
        for vendor in Vendors.select():
            VendorsWithID.create(
                agency_name=vendor.agency_name,
                amount=vendor.amount,
                exclude=vendor.exclude,
                fiscal_year=vendor.fiscal_year,
                payee_name=vendor.payee_name,
                payee_zip=vendor.payee_zip,
                purpose_of_payment_baltimore_county_only=vendor.purpose_of_payment_baltimore_county_only,
                slug=vendor.slug
            )

        # Rename the new table to replace the existing one
        database.execute_sql('ALTER TABLE vendors RENAME TO vendors_old')
        database.execute_sql('ALTER TABLE vendors_new RENAME TO vendors')

# Execute the migration
if __name__ == '__main__':
    migrate_to_new_table()
