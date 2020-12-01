# Unique Design
## Full Stack Frameworks with Django Milestone Project
I have chosen this project to create a website for a friend who like to start his business as graphic designer as basic level. He has provided me with all the detail he has so far for his start-up business and encourage me to complete my project and his website.

My idea is to keep design simple as well as contain provided is not in large quantity but there is scope to improve and more design and service will be added in due course.

### Access my project on Github
https://github.com/hidayatmansuri/uniquedesign

### or Deployed version (Publish version) on Heroku
Unique Design (unique-design.herokuapp.com)

## Technologies
1.	HTML
2.	CSS
3.	JavaScript
4.	Bootstrap 4
5.	Fontawesome
6.	Google Fonts
7.	Snipping Tools
8.	DJango
9.	Stripe
10.	Gmail
11.	Heroku

## UX

This project is simple and easy to navigate where there only handful options available in the main navigation page. Home page describe the service and product company provide. While, another option has all available design to explore and purchase, which leads to choosing option according to customer needs and purchasing as well. Site also have option of saving profile, order history as well as updating person information.

For Example, if some one like to buy Business Card for their business, they can choose from available design which leads customer to choose quantity and paper and site will change price accordingly. On the same page there will be email where they can email details, they like to have chosen design. Once customer is happy with their option(s), they can head on to payment page where they can make payment which will be end with confirmation email as well as customer will have choice of creating profile.

I have kept all the options available on main screen where purchase total will be shown on the right top corner, which help customer keep track of their spending on website. Also, there is a MyProfile link is on main navigation bar too.

## User Stories
### How to choose quantity and paper for a product?
Once customer choose their design, they can click on image provided, which lead them to detail page. On the detail page under the description they will have 2 dropdown boxes, one for quantity and another for paper thickness, which will have add-on price written right next to they chosen options as well as associated product category.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Choose_Quantity_Paper.gif

### How to add to Purchase bag?
Once quantity and paper chosen, on the same page there is a button “Add to Bag”, by clicking or taping on that button, chosen product will be added to Purchase bag which can be confirmed by total on Bag icon on right top corner.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Add_Bag.gif

### How to Remove product from the purchase bag?
Once product added to purchase bag, it can be accessed by clicking on bag icon on right top corner. Once you are on purchase page, just under Add-on option there is option of “Remove”. By clicking or taping on “Remove” link will remove product from your purchase bag.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Remove_Purchase.gif

### How to edit product from the purchase bag?
Once product added to purchase bag, it can be accessed by clicking on bag icon on right top corner. Once you are on purchase page, just under Add-on option there is option of “Edit”. By clicking or taping on “Remove” link will bring customer to edit purchase page where customer can choose Quantity and Thickness again as per their requirement(s).
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Edit_Purchase.gif

### How to make Purchase?
Once product is added on to the purchase bag, you can click on bag icon on right top corner which will land you on Purchase page, where there will be a list of product(s) in purchase bag. On the same page just under Grand Total, there will be a “Secure Checkout” button. By clicking on the button, it will present you with payment page where customer needs to complete personal detail form and card detail. Once form complete customer can click on “Complete Order” button to complete their purchase.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Make_Purchase.gif

### How to Register on the website?
From top navigation bar, there is an option call “My Account”. By clicking or taping on that link customer can access an option of “Register”, which will present customer with a “Sign Up” form. Once required details has been provided and clicked or taped on “Sign Up” button, it will send customer with an email of verifying their account. Once customer receive email and verify their account, customer will be register and can access their profile.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Sign_Up.gif

### How to look at Order History?
Order History can only be accessed if customer have been signed up on website. If customer hasn’t been signed up please check “How to Register on the website?”. Once customer signed up, they can login to their account and Order History will be there on same page as Default Delivery information.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Order_History.gif

### How to Update Delivery Information?
Once customer login to their account, customer can change their personal detail and click “Update Information” link right under delivery information.
https://github.com/hidayatmansuri/simas-recipes/blob/master/media/Update_Delivery.gif

## Features
I have used many Django library on this project which have made accessing data extremely easy.
There is fully feature search bar available, which will help you search for all available product. Also, there is a Combo box for sorting all the product on page, which help customer sorting the products by price and by category. Also, Django context processor have made life very easy, which let developer access data all over site.

## Admin
Important part of this project where I have demonstrated knowledge, I have gain during this module which is to carry out CRUD (Create, Read, Update, Delete) functions. Where admin with superuser rights can make amendment on existing product as well can create new one. With help of Crispy Forms rendering forms are very convenient as well as editing and updating. 

## Feature left to implement

### Amazon AWS S3
I have followed video lesson for this service where I have managed to create bucket as well as connect with database. But when I tried to create media folder within bucket as instructed in video, it won’t allow me for some restriction as well navigating around option are was different than shown in the video which is making even worse to use Amazon AWS S3.

### Design detail
At present customer have to email desired detail they like to have on product. This will be improved with providing input box(es) for customer to put their detail inside. This will provide us detail with order as well as customer do not have to have hassle of emailing detail(s).

## Testing
I have tested this project on number or devices and different browser. I have come across to issues which are loading main image on slow connection and if you have firewall installed it will prompt you with warning that this website is not safe.
For firewall issue I will advise user to carry on with unsafe mode as for now but will in future will improve to have secure environment.
There is an issue of product image, where sometime product image(s) on certain device is not displayed. Have made significant changes to url(s) and models to come over this issue.
I have tested this project on

### Mobile Devices
Pixel 3xl, HTC U12+, iPhone X, Microsoft Lumia 920, HTC U11, One Plus Two, One Plus 7T, iPhone 8, Poco Phone

### Browsers
Google Chrome, Firefox Mozilla, Brave, Opera, Vivaldi, Microsoft Edge browser

### Tablet
iPad Air 2

## Deployment

### Github Deployment Process
1.	Sign in / Sign up on pages.github.com
2.	Create a repository with available name
3.	from AWS Cloud 9 bash run following commands
4.	git init
5.	git add . - to add file(s) to staging area
6.	git commit -m "with message" - commit file(s)
7.	git remote add origin followed by URL (from github website for first time)
8.	git push - followed by username and password to upload file(s) to github

### Deployment to HEROKU
1.	Sign in / Sign up on www.heroku.com
2.	On heroku website create new app with right region
3.	from Gitpod bash run following commands
4.	heroku login - which will prompt with username and password created on heroku website
5.	git status - for status of file(s)
6.	git init
7.	git add . - Add file to staging area
8.	git commit -m "Message" - to commit files with meaningful message which help you in future to understand what changes have been made
9.	heroku git:remote -a project name (for first time)
10.	git remote add heroku URL (Can be achieve from heroku settings)
11.	Add requirement.txt with following command
12.	sudo pip3 freeze > requirements.txt - for list of dependacy of our project
13.	Add procfile with following command
14.	echo web: python run.py > Procfile - Python file which help application mechanism on what command should run
15.	heroku ps:scale web=1 - to scall your web to one running dynos
16.	on heroku website go to APP and SETTINGS
17.	click on reveal config vars where DATABASE_URL, DISABLE_COLLECTSTATIC, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY needs to be added in these fields.
18.	from Gitopd bash run following command to deploy whole app on heroku
19.	git push heroku master
20.	Alternatively, on Heroku website, after clicking you project name, access “Deploy” option, within this page there is “Deployment Method”, where connect with GitHub, which will keep updating Heroku as and when there is depository updated.
21.	Finally, on heroku website go to MORE and Click on RESTART ALL DYNOS
22.	All these steps will make your app available on website which is "appname.herokuapp.com"

## Credit

### Content & Media
All the content and image has been provided by my friend who like me to create his website

### Acknowledgements
I have also used Medium website for some inspiration and ideas for this project as well as Stack Overflow for understanding some functions
