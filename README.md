# Interiorshop

This is an e-commerce app for multiple vendors to list their products (such as furniture), which is created with Django. 
Below are the list of features:

1. Vendor can signup, login and logout. Vendor can edit name or email too.
1. Vendor can post their products ~~with an image~~ (not doable due to the restriction of media file storage in Heroku), title, description and price
1. Vendor can check their product listing, see their balance & paid amount and their order list
1. Buyer can see a list of vendors with each of their product listing
1. Buyer can search the product based on either product title or product description 
1. Buyer can add the order into the cart and then checkout via the cart page
1. The right side of navbar consists of categories listed and a contact page (blank page at the moment)

## Technologies involved:

- Django
- Bulma CSS
- Stripe (Payment gateway)
- Sendgrid (for sending e-mails) *not testable
- PostgreSQL
- Heroku

## Additional Info:

You can login to test the features with below vendor:
> - Username: Test1
> - Password: Test1Test1

Payment testing for Stripe:
> - Card Number: 4242 4242 4242 4242
> - MM / YY: 04 / 24
> - CVC : 242
> - ZIP : 42424

*Notes: Do not add image for product listing


## Deployed under Heroku 
**[Click Here](https://interiorshop.herokuapp.com/)** (Please wait for it to start up from its dormant state)

*Notes: This is a Django practice from a youtube tutorial