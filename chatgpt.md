## How I Used ChatGPT to Build This

Although I had the original boe_spending.db file already, the rest of the app I built with the assistance of ChatGPT 3.5. Here are highlights of that process.

### Setup

I made sure that ChatGPT knew I was building a Flask app using Peewee, and I gave it a copy of my original app.py for context. Then I asked for specific features one-by-one.

### Selected Prompts

* Using Bootstrap, generate an HTML table for the following attributes: agency_name, amount, fiscal_year, payee_name, payee_zip
* make the actual rows (not the header) into a Jinja template for use in a Flask app. each record is called `record`
* For the following app.py, add a search route that redirects to the homepage with a variable called results, where the column to search is payee_name (pasted the app.py file)
* The sqlite database (boe_spending.db) has a vendors table as defined in app.py. Using peewee, write code to generate a table called jurisdictions that consists of the agency_name and slug columns from vendors, along with the total_records for each agency_name and the total_amount representing the sum of amount. Add a Peewee model to app.py.
* Modify the index function so that it gets all of the jurisdictions and returns them to the template in a variable called jurisdictions
* Now modify the index.html template so that it displays the jurisdictions in a two-column table, along with the total records and spending.
* Separate jurisdictions from search results into two different tables
* title case the agency names and add comma styles to the numbers
* add a search form at the top of the index.html template
* Change index.html so that the search bar spans two columns and then in the other two add a drop-down menu listing the jurisdictions and use the jurisdiction slug as the value
* Rewrite the index function in app.py so it provides a list of Jurisdictions in alphabetical order to the template
* In app.py, add a function to handle selections from the drop-down menu by adding a jurisdiction route and function that grabs the specific record from the jurisdictions table and then the associated records from the vendors table
* update the dropdown in index.html to use that new route
* Can I use the form value to redirect to another page?
* Write a jurisdiction.html template that displays the totals for that jurisdiction as feltron numbers and then provides paginated vendor records.
* add breadcrumb navigation to the jurisdiction templates

### Summary

Working iteratively is the key here - trying to do one thing and refining it before moving on to something else. If I made a change in app.py that would result in a new variable being sent to the template, I'd first confirm that it did so and then updated the template to display it. If the display needed some tweaks I did that before moving on.