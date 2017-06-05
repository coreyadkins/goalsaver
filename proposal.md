#Proposal: GoalSaver

*GoalSaver* is a web app that allows users to add and keep track of financial goals.

Once logged in, users will be directed to a home page which will contain "thermometers" for each goal they have inputted, which display how close they are to their goal, and a User Interface to input new goals, and input money saved.

Users can either save for multiple goals simultaneously, choosing how much to split their saved money over each, or queue goals so that they save in a specific order.

Each goal will also display a suggested monthly amount to save for each month, which is the amount needed divided by months until the projected date of completion.

##Specific Functionality

###Login page
All users who are not logged in will be redirected to the login page first, which will display a simple form for them to enter their username and password.

This page will have a link to an account creation page.

###Account creation page
This page will allow a user to create an account by entering in a Username, a password, and a currency type. (Selection in dropdown or entering in via text?)

###Home page
The customized homepage for the user.

This will display the goals they have inputted, divided into "Currently Saving For" and "Future Goals."

The page will have a navigation menu at top with several "buttons," one for "Enter a new goal," and one for "Enter saved amount." Each button will open a window with a form which the user can enter data. A third button "Edit savings distribution" will only become active when there are multiple goals being saved for currently, and will create a window with percentage bars for each goal that will be draggable and adjust based on each others input. A fourth, "Completed Goals" will display just the goals which have been successfully completed.

The users will be able to drag and drop goals to change the order of queuing them. Currently saving goals will be displayed on the leftmost of the scrolling list of goals, and Completed Goals at the rightmost, with Future Goals between the two. Multiple goals will be displayed stacked on top of each other, but occupying the same column. This behavior is only necessary for the "Currently Saving For" column.

Users will be able to click on goals to change their properties, or delete them.

"Currently Saving For" goals will have a colored (green?) thermometer, whereas "Future Goals" will have a gray thermometer and be slightly transparent (or have a gray background to the section.)

At the bottom of the page is a section titled "Remaining amount to save this month to meet goals:" and display the amount needed to reach all current goals this month which have a specified end date (which is the goal amount divided by the amount of months between the current date and the goal). If no current goals have an end-date, this section will not be displayed. If the amount for the month to meet current goals has been met, this section will display "Success! You've saved enough for your goals this month."

Once a goal is met, it will display a "Congratulations!" notification window. That goal will be marked as completed, and moved to the "Completed Goals" section.

When a goal has expired without being completed, the goal thermometer will be outlined in red, and each time the user logs in they will receive a notification window which will ask if they would like to change the end-date or delete the goal, or neither by closing the window.

##Data Model

###Goal
Each Goal is an object containing data entered by the user pertaining to a specific savings goal.
- Unique ID
- User ID
- Name
- Description
- Goal amount
- end-date (optional)
- Amount saved
- Currently saving for (True/false)
- Thermometer color
- Completed (true/false)

###User
Each User will have a Unique ID, which will be used for storing and retrieving their specific goals. They will also have a Currency Type that they choose on account creation, which will affect how their goals will be displayed.
- Unique ID
- Currency Type

##Technical Components
Goal and User models will be stored and searched using Django Models in a PostgreSQL database.

Creation and displaying of goals, and entering of savings, will be handled via a custom UI. Drag and drop reordering of goals will be handled with ReactJS.

Python will be used to generate new Goals.

Thermometers will be displayed using an outside library or module TBD.

##New technologies implemented in this projected
- React for drag and drop reordering

##Future Work
- Build in currency type into goal setup instead of user setup
- Allow multiple currency types between goals, have GoalSaver convert the inputted currency into the various other currencies using current exchange rates.
