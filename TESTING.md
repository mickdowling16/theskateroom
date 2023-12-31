# HTML Testing

I tested all my HTML code using [The W3C Markup Validation Service](https://validator.w3.org/). Below are my results

### Homepage

![homepage html](documentation/testing/html-home.PNG)

### Products

![products html](documentation/testing/html-products.PNG)

### Product detail

![product detail html](documentation/testing/html-product-detail.PNG)

### Events

![events html](documentation/testing/html-events.PNG)

### Event detail

![event detail html](documentation/testing/html-event-details.PNG)

### Event Add

![event add html](documentation/testing/html-event-add.PNG)

### Contact

![contact html](documentation/testing/html-contact.PNG)

### Skateparks

![skateparks html](documentation/testing/html-skate.PNG)

### Checkout

![checkout html](documentation/testing/html-checkout.PNG)

The only error that showed in my html code is the below for a trailing slash. I couldn't identify where in my code this was, it seems to be an issue with the country selector on the profile page. It is the only html error in my code

![html error](documentation/testing/html-error.PNG)

# CSS Testing

To test my CSS file I used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator). I copy and pasted my base CSS file into the validator and it returned a couple of errors.

![base.css erros](documentation/testing/css-errors.PNG)

After I fixed these my base.css code passed

![base.css pass](documentation/testing/css-success.PNG)

I also tested my checkout.css file. This passed first time

![checkout.css pass](documentation/testing/checkout-css-pass.PNG)

# JavaScript Testing

I passed my JS code through [JSHint Code Validator](https://jshint.com/). Below are the results.

My stripe elements js file only had one unused variable. This is the stripe variable that came direclty from the documentation so I left this unchanged as I didn't want to risk breaking by stripe functionality

![stripe elements.js](documentation/testing/stripe-elements-pass.PNG)

The next JS I passed through JSHint was that for my comments section. The only issue was with one line. I tried to fix this error but couldn't get rid of the errors. It seems its an error with the way the template literal is formatted. I decided to leave this in as my comments section works as expected and I didn't want to risk breaking funtionality so close to project submission

![comments js](documentation/testing/comment-js-errors.PNG)

The next JS element I tested was the skateparks map JS. Below is the results, with just one undefined variable, which is from Leaflet library which is defined externally.

![skate maps js](documentation/testing/maps-js.PNG)

# Python Testing

Went through each python file and fixed until no errors were reported in problems terminal. Only issue is line length, but when I tried to fix this it caused more errors in the way the code was read and stopped some of my views from working. Since this was the only errors showing I decided to leave the line length alone as no other problems were showing.

# Manual Testing

1. Main Nav: tested all links on main nav and accessed all pages through the main nav bar. PASSED
2. Search: Tested search functionality and searched for keywords in product name and description. PASSED
3. Log in and out: Tested log in and out function to be able to log into account and then log out of your account. Passed
4. Account registeration: Successfully registered for a new account by filling out registration form.
5. Validate email page: email to validate email address sent. PASSED
6. Product Details: Click each product to show product details page with description, price and add to bag button. PASSED
7. Out of stock: Cannot add out of stock items to bag. PASSED
![Out of stock](documentation/testing/out-of-stock.PNG)
8. Add to bag: Can add in stock items to bag and shopping bag updates with item and bag total. PASSED
![Add to bag](documentation/testing/update-bag.PNG)
9. Update stock levels: When item added to bag stock levels adjust. PASSED
![Update Stock](documentation/testing/update-stock.PNG)
10. Remove items from bag: Click remove button on item in bag and item is removed from the shopping bag. PASSED
11. Product Management: Product can be edited by a superuser by clicking the edit button on product card. PASSED
12. Product Info Populates: Produt information populates the form and admins can edit products. PASSED
![Edit product](documentation/testing/edit.PNG)
13. Delete product: Superuser can permenently delete products from website. PASSED
14. Event management: Superusers can add events when logged in straight from the front end. PASSED
15. Edit event: Superusers can edit events from the events detail page. PASSED
![Event detail](documentation/testing/event-detail.PNG)
![Edit event](documentation/testing/edit-event.PNG)
16. Delete Event: Superusers can permenently delete events. PASSED
17. Register for event: Users can fill out registration form and submit details to admin. PASSED
![Register for event](documentation/testing/register.PNG)
18. Contact form: Users can fill out contact form, form will be submitted and admin will get an email with form contents. PASSED
![Contact form submission email](documentation/testing/contact.PNG)
19. Purchase product: Add products to shopping bag, proceed to checkout, enter details, checkout securely. PASSED
![oder confirmation](documentation/testing/order-confirmation.PNG)
20. Confirmation email: Customer recieves confirmation email after checkout process. PASSED
![oder confirmation email](documentation/testing/order-confirmation-email.PNG)
21. Order history: Customer order history will appear on their profile after ordering. PASSED
![oder history](documentation/testing/order-history.PNG)
22. Newsletter: Users can sign up to be part of our mailing list. PASSED
![Newsletter](documentation/testing/newsletter.PNG)
23. Social Media: Social media icons open up in new tab. Facebook business page connected. PASSED
![Social Media](documentation/testing/social-media.PNG)
![Facebook](documentation/testing/facebook.PNG)
24. Update profile: Fill out form on profile page to update profile information. PASSED
25. Local Skateparks: Click locations to bring user to that point on the map: PASSED
26. Privacy policy: Click privacy policy link in footer to bring me to privacy policy page. PASSED
27. Comments: Go to event details page when logged in, write a comment in the comment box and press submit. PASSED
![Comment](documentation/testing/comment-1.PNG)
![Comment submitted](documentation/testing/comment-2.PNG)
28. Like comment: As a logged in user, like comment in event details page. like number increase by 1. PASSED
![Comment liked](documentation/testing/comment-like.PNG)
29. Register your interest: Click register your interest from event details page. fill out form with details, click submit. PASSED
![Registrations admin panel](documentation/testing/registration-1.PNG)
![Registration email](documentation/testing/registration-2.PNG)


## Browser Compatibility

I tested my site on Chrome, Firefox and Microsoft Edge. All browsers worked as expected with no errors and no differences

## Responsiveness

When testing responsiveness I used my laptop, phone and tablet along with Google developer tools to test the app on different screen sizes. I styles my app with bootstrap to account for smaller screen sizes and for it to be responsive on mobile and tablet. It works as expected on these different screen sizes.

### Mobile

![Mobile Home](documentation/testing/mobile-home.PNG)
![Mobile Events](documentation/testing/mobile-events.PNG)
![Mobile Profile](documentation/testing/mobile-profile.PNG)
![Mobile Shopping](documentation/testing/mobile-shopping.PNG)
![Mobile Products](documentation/testing/mobile-products.PNG)

### Tablet

![Tablet Home](documentation/testing/tablet-home.PNG)
![Tablet Events](documentation/testing/tablet-events.PNG)
![Tablet Profile](documentation/testing/tablet-profile.PNG)
![Tablet Shopping](documentation/testing/tablet-shopping.PNG)
![Tablet Products](documentation/testing/tablet-products.PNG)

## Lighthouse Testing

When I ran my first lighthouse test these were the results below. 

![Lighthouse test 1](documentation/testing/lighthouse-test-1.PNG)

On the second test these were my results. My accessibility score increased as I added aria labels to my social media links and my search button, but my performance score decreased for an unknown reason as nothing else was changed

![Lighthouse test 2](documentation/testing/lighthouse-test-2.PNG)

When I fixed some of my errors in the html validator my lighthosue score increased further

![Lighthouse test 3](documentation/testing/lighthouse-test-3.PNG)


## Bugs

### Unsloved bugs

- On my skateparks locator page, the coordinates aren't 100% accurate. I'm not sure why this has happened. I got the correct coordinates from Google maps and plotted them on the map. When doing some research it could be a issue with the map supplier I used, Leaflet. I decided to leave this bug as for the purpose of this project it does the job as intended but for a real life website I would have to make sure this information is accurate. I would probably use Google maps as my supplier for this, but Leaflet was easy to set up and fit the purpose of the project.

- Another unsolved bug on my site is that of the stock control. I implemented stock control for my products and for the inventory to automaticallty update if a product is added to the bag. An issue I had was trying to implement different stock values for each size of clothing. I tried to do this but when I changed my products model and views I kept running into errors with the way the template was rending the out of stock message. This problem took up a considerable amount of time and unfortunately I had to leave it and move onto something else in order to complete the project in time. I reverted back to the old code I had, so stock will update and each otem has a stock value, but unfortunetly I couldn't allocate a stock value for each different size as I couldn't solve the bug

### Solved bugs

- One solved bug that I had was when implementing by comments section on my events page. The comments would submit but not appear in the comments section. I solved this by using javascript to reload the page and clear the comment box when the submit button is clicked, the javascript also handles comment likes. My comment section now works as intended.