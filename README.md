# Maryland School Board Spending App 

In this project, I've developed a Flask-based web application designed to provide users with access to spending records from various Maryland school boards. The application includes essential features like searching for specific payees, browsing through spending records, and displaying total spending for each jurisdiction.

To manage the data efficiently, I've leveraged the Peewee ORM, which streamlines interactions with the SQLite database. One notable aspect is Peewee's ability to handle primary keys automatically, which simplifies working with existing databases.

On the front end, the user interface is crafted using HTML templates powered by Jinja2. I've utilized Bootstrap components to enhance the aesthetics and added breadcrumb navigation for intuitive page navigation.

Overall, this application serves as a valuable tool for users interested in exploring spending data. It offers a user-friendly interface and essential features to facilitate easy access and analysis of jurisdictional spending records.

### Guide to app imports and setup

Imports:

1. `Flask`: This import brings in the Flask framework, which is used to create and manage the web application.

2. `render_template`: This import allows us to render HTML templates within Flask routes, enabling dynamic content generation.

3. `request`: This import provides access to incoming request data, such as form submissions or URL parameters.

4. `redirect` and `url_for`: These imports are used to perform URL redirection within Flask routes.

5. `SqliteDatabase`: This import is from the Peewee library and enables connection to an SQLite database.

6. `Model`: This import is also from Peewee and serves as a base class for defining database models.

Model Definitions:

1. `BaseModel`: This class inherits from Peewee's `Model` class and acts as a base model for other models. It's used to specify the database connection for all models.

2. `Vendors`: This model represents the vendors table in the database. It defines fields such as agency name, amount, payee name, etc. It also specifies the table name and that there is no primary key explicitly defined.

3. `Jurisdiction`: Similar to the Vendors model, this represents the jurisdictions table. It defines fields like agency name, slug, total records, and total amount. Again, no primary key is explicitly defined.

### Guide to app.py functions

1. `index()`: This function handles the route for the homepage. It retrieves all jurisdictions from the database and orders them by agency name. Then, it renders the `index.html` template, passing the jurisdictions as context.

2. `search()`: This function handles the search form submission. It retrieves the search term entered by the user and queries the vendors table to find records containing the search term in the payee name. The search results are then ordered by the amount and rendered back to the `index.html` template.

3. `redirect_to_jurisdiction()`: This function is triggered when the user submits a form to navigate to a specific jurisdiction page. It retrieves the slug of the selected jurisdiction from the form data and redirects the user to the corresponding jurisdiction page using the `jurisdiction()` route.

4. `jurisdiction(slug)`: This function handles the route for displaying jurisdiction details. It takes the slug of the jurisdiction as a parameter, retrieves the jurisdiction details from the database based on the slug, and fetches associated vendor records. Finally, it renders the `jurisdiction.html` template, passing the jurisdiction and vendor records as context.

### Run the app in Codespaces

Create a codespace, then in the terminal run the following commands:

1. pip install -r requirements.txt
2. python app.py

