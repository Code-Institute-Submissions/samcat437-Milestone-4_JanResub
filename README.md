# Vintage Sound Ecommerce Application

This application will user's to browse products, login and create a profile, add and delete them to their wishlist, shopping bag, checkout with Stripe, receive an email confirmation, write a review of the product and log out. Admin users are able to add, update and delete items on the website.

View the live link here. 

# User Experience

## User Stories

View the project's users stories: 

[Admin and Store Management](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Admin%20and%20Store%20Management.png)

[Purchasing and Checkout](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Admin%20and%20Store%20Management.png)

[Registration and User Accounts](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Registration%20and%20User%20Accounts.png)

[Reviews](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Reviews.png)

[Sorting and Searching](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Sorting%20and%20Searching.png)

[Viewing and Navigation](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Viewing%20and%20Navigation.png)

[Wistlist](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Wishlist.png)

## Features

### Navbar and Footer

1. Navbar will be at the top of all pages on the desktop version once logged into the portal.
2. Navbar on desktop will display all options. On mobile, once the hamburger is clicked, the navigation options will appear.
3. Navbar will have the following options if logged in: 
    * My Wedding
    * Reviews
    * Log out 
3. Clicking on the relevant navigation option will redirect the user to that page.

4. Footer will be sticky. Navbar will be responsive and fill the entire width of small screens.
 
 
### Home Page

1. The home page will welcome users to the store and have a useful navigation bar to access the site. 
2. A large button will direct the user to the All Products page where they can quickly start browsing and making purchases.

### Nav Bar

## For Non-authenticated Users : 

1. The nav bar will provide links to all the products and sort them by category.
2. Non-authenticated users will see a Login and Register button under 'My Account'.
3. There will be a search bar (collapsable on mobile) for querying the store database.
4. The shopping bag will display the shopping bag.

## For Authenticated Users : 

1. The My Account nav element will show Product Management, My Profile, My Wishlist, and Log out options.

### My Wishlist

1. When a user clicks on a product, they will be able to click on the "add to wishlist" option.  
2. They will receive a notification that they item has been added to their wishlist, or that the item is already in the wishlist. 
3. They can then click on the link "View Wishlist" or click on "My Wishlist" in the navigation menu.
4. Once navigating to their Wishlist, a user can view and delete the Wishlist as appropriate.
5. The user can add the item directly to their bag.

### Reviews 

1. When clicking on a product, a user is able to view previously written review by other users.
2. If the user has purchased the product, they will be able to write a review of the product.
2. If the user is the author of the review, they will be able to edit or delete their review.
3. The user is able to navigation to the "My Reviews" page in order to view, edit and delete their review in one place.

## Design

### Colour Scheme 

Purple and black are the main colors on the site that compliments the main image on the home page.

## Typography 

Audiowide font was sourced from Google Fonts to create a vintage, 80s look.

### Images 

The main image on the home page is [here](https://www.freepik.com/free-photo/closeup-man-playing-bass-guitar_21782474.htm#query=rock%20and%20roll%20male%20musician%20bass%20guitar&position=5&from_view=search&track=sph). Image is by pvproductions on Freepik.


## Wireframes 

### Technologies

## Languages Used

[HTML 5](https://en.wikipedia.org/wiki/HTML5) : HTML 5 was the main language used across the site.

[CSS 3](https://developer.mozilla.org/en-US/docs/Web/CSS) : CSS 3 was used to style the site.

[Javascript ES6](https://www.w3schools.com/js/js_es6.asp) : Javascript ES6 was used to operate Stripe payment processing. 

[Python3](https://www.python.org/) : Python3 was the main programming language used to create routes, models and logic in conjunction with Flask in order to render the site.

[Jinja](https://flask.palletsprojects.com/en/2.1.x/) : Jinja is used to create templates to populate HTML pages on the site.

### Frameworks Used

[Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction//) : Bootstrap was used to structure the html pages.

[Django](https://www.djangoproject.com//) : Django is the high-level Python framework used to structure the application.

[Python3](https://www.python.org/) : Python is the programming language that the views, models, urls, admin and apps.py is written.

[Google Fonts](https://fonts.google.com/) : Google Fonts provided the font "Nanum Gothic" and "Gochi Hand" in order to customise and stylise the text. 

[Coolors](https://coolors.co/) : Coolors is a colour palette generator I used to create colours that worked together for the site.

[Git](https://git-scm.com/) : Git is the technology that hosts the Gitpod IDE and terminal where the project was coded. Git then committed and pushed the code to the cloud-based servers on GitHub.
 
[GitHub](https://github.com/) : GitHub hosted the project on its servers after being pushed by Git.

[Balsamiq](https://balsamiq.com/) : Balsamiq was used to create and download wireframes for the project.

[Fontawesome](https://fontawesome.com/kits) : Font Awesome is a database of icons that can be used for visual interest.

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) : Chrome Dev tools were utilised for the Javascript console as well as to verify the site's responsiveness and visual presentation. 

### Bugs

## Testing 

### Code Validation 

The W3C Markup Validator, W3C CSS Validator, Jshint and Pep8 Services were used to check each page for syntax errors. 

[W3C Markup Validator](https://validator.w3.org/)



[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 



[Jshint](https://jshint.com/) 



[Pep8online](http://pep8online.com/)


## Manual Testing 

Manual tests were conducted throughout the development process via the python terminal to understand the UX, routing and data population features.


### Test Cases based on User Stories



## Deployment 

### Via Heroku 

I used Heroku.com to host my app. This website ran the python code and produced a live link which can be found [here](). Heroku connects to GitHub and with every push updates the site on Heroku.

1. In the gitpod terminal, a requirements.txt and a Procfile are first created by using the following commands:
pip3 freeze –local > requirements.txt and echo web: python app.py > Procfile
2. The new files are then committed to GitHub.
3. In Heroku.com, a new account is created, followed by a new app. Europe is then chosen as the region nearest geographically for free service. Amazon Web Services were also chosen as the provider.
4. Next, the Deployment Method of Connecting to GitHub is selected.
Within the search bar, the repository name is entered and the correct repository (Milestone-4) is selected to connect via the button. Automatic deploys are enabled from the main branch.
5. In the settings tab, the Config Vars information needs to be filled out very carefully. If these contain discrepencies, the app will not run. These included the following fields: DATABASE_URL, HEROKU_POSTGRESQL_RED_URL, IP, MONGO_DBNAME, MONGO_URI, PORT and SECRET_KEY. These fields correspond to the respective MongoDB, Heroku Postgresql add-on, Port and IP information as appropriate for your project. These are not disclosed her for security of the site.
6. "Deploy Branch" was selected and the app is successfully built. 

### Via Gitpod ran locally

1. Navigate to the Github repository at [here]().
2. Choose "Gitpod."
3. In the Bash terminal, type: `python3 manage.py runserver`
4. Choose "Make Public" when a blue button appears.
5. Choose "Open Browser" when the options appears.

### Acknowledgements

Massive thanks to my Code Institute mentor for guiding me through the development process. Thank you to tutor support for being patient during tutoring sessions. 