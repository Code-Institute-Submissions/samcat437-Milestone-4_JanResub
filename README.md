# Vintage Sound Ecommerce Application

This application will user's to browse products, login and create a profile, add and delete them to their wishlist, shopping bag, checkout with Stripe, receive an email confirmation, write a review of the product and log out. Admin users are able to add, update and delete items on the website.

View the live link here. 

# User Experience

## User Stories

| User Story ID  | As a/an  | I want to be able to...  | So that I can... |
|---|---|---|---|
| Viewing Products & Navigation |
|   | User/Shopper | View a list of products | Select it for purchase. |
|   |   | View individual product details | Identify the price and description of the item. |
|   |   | Easily view the total of my purchases at any time | Ensure that the total is correct. |
|   |   | View a specific category of products | Quickly find products I’m interested in without having to search through all the products. |
| Sorting and Searching |
|   | User/Shopper | Sort the list of available products | Easily identify the products by type. |
|   |   | Sort a specific category of product | Find the product by year or era. |
|   |   | Search a product by name or description | Find a specific product I’d like to purchase. |
|   |   | Easily see what I’ve searched for and the number of results | Quickly see if the product I want is available. |
| Purchasing and Checkout |
|   | User/Shopper | search for specific products | find products I am interested in buying. |
|   |   | easily understand the search results | quickly decide which product I want to buy. |
|   |   | sort by price, name, category and rating  | view a wide range and choose which to buy. |
| Checkout  |
| | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive. |
|   |   | Adjust items in my bag to be purchased | Easily make changes to my purchase before checkout. |
|   |   | Enter payment information | Check out quickly with no hassles. |
|   |   | Feel that my personal and financial information is safe and secure | Confidently provide the needed information to make a purchase. |
|   |   | View an order confirmation after checkout | Keep this confirmation for my records. |
| Admin and Store Management  |
|   | Store owner/Admin | Add a product | Add new items to my store  |
|   |   | Edit and update a product | Change product prices, description, images and other product criteria |
|   |   | Delete a product | Remove items that are not for sale. |
| Reviews  |
|   | User | Add a review (Create) | Comment on the item so that other shoppers can receive feedback regarding the item / ask questions to the store owner  |
|   |   | Read the review | View the comment on the item |
|   |   | Update the review | Change the content of the comment if author. |
|   |   | Delete review | Delete the review if desired and if author. |
| Registration and User Accounts  |
|   | User | Easily register for an account | Have a personal account and be able to view profile.  |
|   |   | Easily login or logout | Access personal account information. |
|   |   | Easily recover password | Recover access to account. |
|   |   | Receive email confirmation after registering | Verify account registration was successful. |
| Wishlist  |
|   | User | Select a product to add to Wishlist (Create) | Click the button to add to Wishlist  |
|   |   | View the Wishlist in the profile (read)| Save the product to a list in the product description and within profile |
|   |   | Remove the item from Wishlist (Edit/delete) | Change the wish list as desired. |

View the project's users stories on Github: 

[Admin and Store Management](https://github.com/samcat437/Milestone-4/blob/main/docs/user_stories/Admin%20and%20Store%20Management.png)

[Purchasing and Checkout](https://github.com/samcat437/Milestone-4/blob/main/docs/user_stories/Admin%20and%20Store%20Management.png)

[Registration and User Accounts](https://github.com/samcat437/Milestone-4/blob/main/docs/user_stories/Registration%20and%20User%20Accounts.png)

[Reviews](https://github.com/samcat437/Milestone-4/blob/main/docs/user_stories/Reviews.png)

[Sorting and Searching](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Sorting%20and%20Searching.png)

[Viewing and Navigation](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Viewing%20and%20Navigation.png)

[Wistlist](https://github.com/samcat437/Milestone-4/blob/main/media/user_stories/Wishlist.png)

## Credientials 

Super User: 
username: samcat437
password: samcat437

## Features to support User Stories

### Navbar

1. Navbar will be at the top of all pages on the desktop version once logged into the portal.
2. Navbar on desktop will display all options. On mobile, once the hamburger is clicked, the navigation options will appear.
3. Navbar will have the following options if logged in: 
    * My Profile
    * My Wishlist
    * My Reviews
    * Log out 
4. If user is a superuser, they will also have the Project Management option.
5. If user is not logged in, they will only have two options: 
    * Register
    * Login
6. Clicking on the relevant navigation option will redirect the user to that page.

7. Navbar will be responsive and fill the entire width of small screens.
 
### Home Page

1. The home page will welcome users to the store and have a useful navigation bar to access the site. 
2. A large button will direct the user to the All Products page where they can quickly start browsing and making purchases. 
3. A user may click on a product to view more details about the product. 

## Navbar

## For Non-authenticated Users : 

1. The nav bar will provide links to all the products and sort them by category.
2. Non-authenticated users will see a Login and Register button under 'My Account'.
3. There will be a search bar (collapsable on mobile) for querying the store database.
4. The shopping bag will display the shopping bag.

## For Authenticated Users : 

1. The My Account nav element will show Product Management, My Profile, My Wishlist, My Reviews, and Log out options.

## How are the User Stories met across the site?

### Admin and Store Management

1. Superuser have a Product Management link in their navigation.
2. Clicking on this directs them to a form where they can add a product. 
3. On the products page or product detail page, a superuser has access to the edit form, prefilled with the existing data, and the ability to edit it. 
4. On the same pages, the superuser can delete a product. 

### Purchasing and Checkout

1. Shoppers can view their bag at any time by clicking the bag icon in the nav bar. This is totalled so they can see their total. 
2. In the bag, they can remove items. 
3. on the checkout page, the user is able to fill out their payment information through Stripe.
4. After checkout, the order information is saved to the user's profile. 

### Registration and User Accounts

1. Users are directed through Allauth to register for an account.
2. Logging in and out is easy via allauth after clicking on the appropriate link in the navbar.
3. Users are able to recover their password through Allauth.
4. Registered users can save their delivery information on their profile as well as view orders, wishlists, and reviews in one central location. 

### Reviews 

1. Users are able to review their orders via their profile page by clicking on add review. 
2. When clicking on a product, a user is able to view previously written review by other users.
3. Users can read their reviews on their review page.
4. A user can edit their review by clicking edit review on their review page.
5. A user can delete their review by clicking delete and confirming.

### Sorting and Searching

1. Users are able to sort and search products via the navigation at the top of the page, including by category.
2. Users are able to search with key words using the search bar.

### Viewing and Navigation

Users are able to use the product filter, shop bag and profile link to view navigation over the site.

### My Wishlist

1. When a user clicks on a product, they will be able to click on the "add to wishlist" option.  
2. They will receive a notification that they item has been added to their wishlist, or that the item is already in the wishlist. 
3. They can then click on "My Wishlist" in the navigation menu.
4. Once navigating to their Wishlist, a user can view and delete the Wishlist as appropriate after confirmation.

## Design

### Colour Scheme 

Purple and black are the main colors on the site that compliments the main image on the home page.

## Typography 

Audiowide font was sourced from Google Fonts to create a vintage, 80s look.

### Images 

The main image on the home page is [here](https://www.freepik.com/free-photo/closeup-man-playing-bass-guitar_21782474.htm#query=rock%20and%20roll%20male%20musician%20bass%20guitar&position=5&from_view=search&track=sph). Image is by pvproductions on Freepik.

All product images and data have been photographed by myself.

## Wireframes 

Wireframes can be found in docs/wireframes. 

They are as follows: 
1. Products Page
2. Wishlist List
3. Wishlist Confirmation (deletion)
4. Profile
5. Add Review
6. Edit Review

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

[Git](https://git-scm.com/) : Git is the technology that hosts the Gitpod IDE and terminal where the project was coded. Git then committed and pushed the code to the cloud-based servers on GitHub.
 
[GitHub](https://github.com/) : GitHub hosted the project on its servers after being pushed by Git.

[Balsamiq](https://balsamiq.com/) : Balsamiq was used to create and download wireframes for the project.

[Fontawesome](https://fontawesome.com/kits) : Font Awesome is a database of icons that can be used for visual interest.

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) : Chrome Dev tools were utilised for the Javascript console as well as to verify the site's responsiveness and visual presentation. 

## Bugs

### Fixed Bugs

During development, I struggled with my wishlist model. I overcomplicated the model with a many to many relationship which I had to redo. I ended up deleting the entire app and started again, but it seemed like I had old data in my database after deletion. Tutor support helped me delete every migration file in the app and remigrate the database. This took a few tries, but finally the database was stable.

I had an issue with the S3 bucket loading images. It ended up having added another file extension of ".JPG" onto my images that alrady had ".jpg" there. It took trial and error and reading of documentation to see that the bucket preferes lower case ".jpg". Changing it to this solved the issue. 

I had some problems with my wishlist views accessing correct variables and urls. I was getting an 404 error that the path could not be found. It turned out that I needed an ending slash on my wishlist/urls.py path. 

### Remaining Bugs

The UI could be improved on the profile page. At the moment, it is a bit messy. Perhaps some of the order fields could be removed and the Add Review link more attractive. On the products page, the smaller images are not in-line with the bigger ones which is not visually attractive. 

### Future Features

I would like to add a toggle to the wishlist list button, so that if clicked, it will be disabled and the message telling users that the item already exists will not be needed. I would like to add javascript to the button so that it turns pink when selected. 

I would like to add functionality so that if a product has been reviewed, it will be displayed on the product detail page, so that it is more useful to users. Having it in a separate review page isn't helpful, but this served as a coding exercise. 

I would like to remove the option of quantity in a future version as there is only one unique item available.

## Testing 

### Code Validation 

The W3C Markup Validator, W3C CSS Validator, Jshint and Pep8 Services were used to check each page for syntax errors. 

[W3C Markup Validator](https://validator.w3.org/)

I validated my code for the templates that I wrote, review.html, confirmation.html, wishlist.html, add_review.html and edit_review.html. There were similar errors picked up by the validator regarding the django templating language. It seems like it can be largely ignored. 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

Valid CSS can be found in docs/code_validation.

[Jshint](https://jshint.com/) 

Not a lot of JS was used in this project, and this was taken from the Stripe documentation via the Code Institute tutorial. 

[Pep8online](https://www.tutorialspoint.com/online_python_formatter.htm)

This site was used to beautify the python code. However, when fixing long lines, the code seemed to break so I have left it as is to ensure the program works for submission.

## Manual Testing 

Manual tests were conducted throughout the development process via the python terminal to understand the UX, routing and data population features.

Test screenshots with descriptive titles can be found in the docs/testing folder. Testing was carried out on devices of various screen sizes. 

## Deployment 

### Via Heroku 

I used Heroku.com to host my app. This website ran the python code and produced a live link which can be found [here](https://milestone-4-vintage-sound.herokuapp.com/). Heroku connects to GitHub and with every push updates the site on Heroku.

1. Log in to Heroku and create a new app by clicking "New" and "Create New App", naming and setting the region to closest to your location.
2. Click on Heroku Resources and add Postgres using the free plan.
3. In the IDE, create or update a requirements.txt file using command pip3 freeze > requirements.txt
4. Create a Procfile with the terminal command web: gunicorn vintage_sound.wsgi:application. Be sure there is no blank line at the end.
5. Use the loaddata command to load the fixtures for both json files: python3 manage.py loaddata categories.json and python3 manage.py loaddata products.json
6. If it returns error message: django.db.utils.OperationalError: FATAL: role does not exist run unset PGHOSTADDR in your terminal and run the commands in step 10 again.
7. From the CLI, login to Heroku using command heroku login -i.
8. Temporarily disable Collectstatic by running: heroku:config:set DISABLE_COLLECTSTATIC=1 --app So that Heroku won't try to collect static files when we deploy.
9. Add Heroku app name to ALLOWED_HOSTS in settings.py.
10. Commit changes to GitHub using git add ., git commit -m , git push. Deploy to Heroku using git push heroku main. If the git remote isn't initialised you may have to do that first by running *heroku git:remote -a
and create a superuser using command: heroku run python3 manage.py createsuperuser so that you can login to admin as required.
11. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub".
12. Search for your GitHub repo and connect then Enable Automatic Deploys.
13. Generate secret key. Strong secret keys can be obtained from MiniWebTool. This automatically generates a secret key 50 characters long with alphanumeric characters and symbols.
14. Add secret key to GitPod variables and Heroku config vars.
15. Set up Amazon AWS S3 bucket.
16. In the dashboard click "Settings" -> "Reveal Config Vars"
17. Set config vars using advice below.

#### **Amazon AWS**

1. Create Amazon AWS account and create a new bucket in the S3 services and choose your closest region.
2. Uncheck block all public access and create bucket. 
3. From the Properties tab turn on static website hosting using default values of index.html and errors.html.
4. On permissions tab include CORS configuration:
```python
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Create security policy: S3 Bucket Policy, allow all principles by adding a * and Amazon S3 services and selecting Get Object action. Paste ARN from Bucket Policy, add statement, generate policy and copy and paste into Bucket Policy. Also add /* at end of resource key to allow use of all pages. 
6. Under public access select access to all List Objects. 
7. Create Group for the bucket through IAM. Create policy by importing AWS S3 Full Access policy and add ARN from bucket to the policy resources. Attach policy to group. 
8. Create user, give programmatic access and add user to the group. Download CSV file when prompted to save access key ID an secret access key to save to environment and config [variables](#config-vars).
9. Add AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME = 'eu-west-2' to settings.py.
10. Add, commit and push to GitHub then navigate to Heroku to confirm static files collected successfully on the Build Log. The DISABLE_COLLECTSTATIC variable can now be deleted. 

### **Config Vars**

The config/environment variables should be set up as follows:

| Key                    | Value                      |
| ---------------------- |--------------------------- |
| PORT                   | 8000                       |
| IP                     | 0.0.0.0                    |
| SECRET_KEY             | YOUR_SECRET_KEY            |
| STRIPE_PUBLIC_KEY      | STRIPE_PUBLIC_KEY          |
| STRIPE_SECRET_KEY      | YOUR_STRIPE_SECRET_KEY     |
| STRIPE_WH_SECRET       | STRIPE_WEBHOOKS_KEY        |
| DATABASE_URL           | YOUR_POSTGRES_URL          |
| AWS_ACCESS_KEY_ID      | YOUR_AWS_ACCESS_KEY_ID     |
| AWS_SECRET_ACCESS_KEY  | YOUR_AWS_SECRET_ACCESS_KEY |   
| USE_AWS                | True                       |
| EMAIL_HOST_PASS        | YOUR_EMAIL_HOST_PASSCODE   |
| EMAIL_HOST_USER        | YOUR_EMAIL_HOST_USERNAME   |


### Via Gitpod ran locally

1. Navigate to the Github repository at [here](https://github.com/samcat437/Milestone-4).
2. Choose "Gitpod."
3. In the Bash terminal, type: `python3 manage.py runserver`
4. Choose "Make Public" when a blue button appears.
5. Choose "Open Browser" when the options appears.

### Acknowledgements

Massive thanks to my Code Institute mentor for guiding me through the development process. Thank you to tutor support for being patient during tutoring sessions. 