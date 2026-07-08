# Smiple Roller Coaster Database 

This is a simple program that runs using python and SQLite. In the python script, the user will be able to use CRUD operations to manipulate the data in the table. A table called "mini_coasters.db" is created. It contains an ID, coaster name, park name, speed (mph) and inversion count. 

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the repo
2. Open VS Code 
3. Install the SQLite and SQLite View extensions
4. Open the project folder
5. Press the "RUN" button.

Instructions for using the software:

1. **View All Coasters (READ):** Press '1' to display all the coasters that are listed in the database.
2. **Add New Coaster (CREATE):** Press '2' to the creation prompt. From there, the terminal will prompt for a coaster name, park name, speed, and inversion count. Once you finish with all prompts, it will then be added to the 'coaster' table.
3. **Update Coaster (UPDATE):** Press '3' to update a coaster. The user can update the name of park/coaster, speed, or inversion count if they entered incorrectly. This will then save and update the database.
4.**Remove Coaster (DELETE):** Press '4' to delete a coaster. The menu will show the list of coasters and will prompt the user to enter in the ID of the coaster wanting to be deleted. It will then delete the coaster and all data regardning that coaster from the database.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.11+
* SQLite 3
* VS Code or PyCharm


## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
* [W3 School SQL](https://www.w3schools.com/sql/)
  

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:
* Add more tables for things such as parks, roller coaster manufacturers, and coasters all linked together through foreign keys.
* I would add a more tighter exception handling to catch things such as negative integers or bad strings.
* Add advanced filters to see the top coasters depending on a certain condition, such as fastest speed, most inversions, etc.

