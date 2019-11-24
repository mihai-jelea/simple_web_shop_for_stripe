# Simple Shopping Cart integrated with Stripe

## Authors

* **Mihai Jelea**  
mihai.jelea@gmail.com  |  +31 641 786 247


## Context

As part of the recruitment process with Stripe, I was required to build a simple proof-of-concept application that would demonstrate [Stripe's API](https://www.stripe.com/) plug-and-play integration capabilities with an online shopping store:
* Easy to set up
* Easy to use
* Reliable
* Secure
* Scalable


## Instructions

Create a simple e-commerce application using Stripe's APIs and your favorite language, along with a doc outlining details about your design and implementation (below). It's important to note that this exercise should take a few hours at most — we only want to assess your ability to design a program, write some code, and explain it. 

Your output should be a simple program that allows the user to take a few actions:

1. Add an item to a shopping cart
2. Checkout and purchase the item using Stripe. 
3. Display a confirmation of purchase to the user with the total amount of the charge and Stripe charge ID (beginning with ch_). 

We encourage you to use the stack you're most comfortable with, but find that the best project submissions use simple frameworks (e.g. Express, Sinatra, Django, etc.). We're also not grading your front-end design skills, so no need to spend a lot of time perfecting your CSS. 


## Implementation Summary

I consider that the most important skill that I possess is the ability to quickly adapt to and learn new technologies. My entire professional career, so far, was based on this. I’ve worked on a lot of projects that involved distinct technology stacks.  I’ve gone through a lot of languages (from C, to C++ and C#, Java, Javascript, Python, SQL and much more) , operating systems (a bunch of Linux distros), databases (from Oracle to mySQL to SQL Server to Google BigQuery) and cloud infrastructures (all the biggest players: AWS, GCP, Azure).  
Now, taking all of this in account and the fact that several framework were suggested in the instructions I decided to implement the application in Python, using the Django framework. I’ve chosen Python because I haven’t been using it in the past 3 years and I wanted to refresh my memory. Also, I decided to use a framework in which I had no previous experience. 


## Built With

* [Python](https://www.python.org/) - Besides the reasons already provided, I've chosen Python because for this specific task because I needed something simple and reliable that would get the job done fast (and so I decided not to reinvent the wheel, but to take advantage of the extensive open source library)
* [Django](https://www.djangoproject.com/) - I decided to do some research and to find the most suitable Python framework for this job. And I decided to go with Django for the following reasons: perfect for e-commerce websites, comes with a lot of features out-of-the-box and has a very large active community surrounding it and constantly improving it. 
* [Bootstrap](https://getbootstrap.com/) - Because me and front-end development don't get along that well, I've decided to use Bootstrap, so that the User Interface will be *almost* decent.


## Setup

Steps I performed in order to have a development environment to start building, testing and running the app:
1. Create a VM on MS Azure, with Ubuntu Server running on it
2. Installed Python + Pip
3. Created a virtual environment in which to build, test and run the application
4. Installed Django in the virtual environment
5. Installed all the apps needed in the virtual environment (you can find all of them in requirements.txt file)
6. Installed latest version of Stripe library in the virtual environment
7. Installed Visual Studio Code (Microsoft's IDEs rock!)


## Implementation Details

After having my development environment ready, I started out testing the Django framework by building several small apps. Afterwards, I found some tutorials that explained how to build a shopping cart app. After that, I found tutorials on how to integrate Stripe into Django. 

I’ve used the Stripe’s exhaustive documentation in order to learn how it works and what must be done in order to use it in my app. 

I’ve decided to use the Charges API and followed the documentation provided here: https://stripe.com/docs/payments/accept-a-payment-charges#python

It all went really smooth. 

The checkout page uses html, css and javascript code blocks copied from Stripe documentation page. 

Getting into details, we have the following modules:
1. Root module "cart". This is the Django root app: contains the system settings, urls, environmental variables.
2. The "products" module handles the products page and the product entity (data structure). A product must have a name and a price. It as also receives and auto ID when it gets created. Currently there is no function exposed in order to create new products. There is only one product in the database - for splicity.
3. The "shopping_cart" module handles all the operations supported by the web store: adding a product to the cart, proceeding to checkout, order summary, deleting the cart contents.


## Installing & Running the Application

First of all, you need to set up an enviroment (ideally virtual) and install all the prerequisites found in the project's requirements.txt.

To do that, simply run the following command in a terminal: **pip install -r requirements.txt**

Afterwords, all you have to do is run the following command in the root of the project, to start the app (make sure port 8000/tcp is free): **python manage.py runserver**

Now that the app is running, go to http://127.0.0.1:8000/products/ and start using it. 

This app uses my Stripe API Keys. 


## Extending the Application

This is only a proof-of-concept application and is lacking a lot of features/functionality that is preventing it to go into production. 

The major problem with it is security. It lacks an authentication module that would have to provide the following:
-	Ability to Register & create a user account
-	Ability to sign in
-	User profiles

It also lacks a lot of important but basic features for a web store:
1.	A product catalogue
2.	Order management and history
3.	Transactions management and history
4.	More payment methods
5.	The ability to securely store the card details into the user profile 

Also, in terms of Stripe integration, it would need switching from the Charges API to Payment Intents API, in order to allow customers from outside US and Canada to be able to pay. 

