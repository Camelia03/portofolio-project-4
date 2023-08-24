# Testing

Return back to the [README.md](README.md) file.

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [Jigsaw Validator](#Jigsaw-Validator)
  * [JavaScript Validator](#JS-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)
  * [Python-Unit testing](#Python-Unit-testing)

* [MANUAL TESTING](#MANUAL-TESTING)
  * [Testing User Stories](#Testing-User-Stories)




## AUTOMATED TESTING

### W3C Validator
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.

**HTML results:**

The following pages were tested and no errors were detected on any of the pages:

[Home Page W3C HTML Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffoundintranslationsodaci.herokuapp.com%2F)
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_homepage.png)
</details>

- - -

[Log In W3C HTML Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgo-global-011c0a1d1612.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2F)
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_login.png)
</details>

- - -

[Sign Up W3C HTML Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgo-global-011c0a1d1612.herokuapp.com%2Fforum%2Fsignup)
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_signup.png)
</details>

- - -

[Reset Password V3C HTML Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgo-global-011c0a1d1612.herokuapp.com%2Faccounts%2Fpassword_reset%2F)
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_resetpassword.png)
</details>

- - -

[Add thread V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_addthread.png)
</details>

- - -

[Channels V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_channels.png)
</details>

- - -

[Edit Profile V3C HTML Validation]()
<details>
<summary>Validation Passe</summary>

![screenshot](docs/validation//html_validation_editprofile.png)
</details>

- - -

[Edit thread V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_editthread.png)
</details>

- - -

[My Profile V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_myprofile.png)
</details>

- - -

[My threads V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_mythreads.png)
</details>

- - -

[Order By V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_orderby.png)
</details>

- - -

[Search V3C HTML Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/html_validation_search.png)
</details>

- - -

### Jigsaw Validator
The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website.

 **CSS Validation**

The testing of the `style.css` file resulted in the following outcome:

[W3C Jigsaw CSS Validation]()
<details>
<summary>Validation Passed</summary>

![screenshot](docs/validation/css_validation_noerrors.png)
</details>

- - -

### JS Validator

[JSHint](https://jshint.com/) was used to validate the JavaScript of the website.

[JSHint Validation]()
<details>
<summary>index.js - Validation Passed</summary>

![screenshot](docs/validation/js_validation_index.png)
</details>

- - -

[JSHint Validation]()
<details>
<summary>user_threads.js - Validation Passed</summary>

![screenshot](docs/validation/js_validation_userthreads.png)
</details>


### Python Validator

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.


<details>
<summary>forms.py</summary>

![screenshot](docs/validation/py_validation_forms.png)
</details>

- - -

<details>
<summary>models.py</summary>

![screenshot](docs/validation/py_validation_models.png)
</details>

- - -

<details>
<summary>signals.py</summary>

![screenshot](docs/validation/py_validation_signals.png)
</details>

- - -

<details>
<summary>tests.py</summary>

![screenshot](docs/validation/py_validation_tests.png)
</details>

- - -

<details>
<summary>urls.py (main)</summary>

![screenshot](docs/validation/py_validation_urls_main.png)
</details>

- - -

<details>
<summary>views.py</summary>

![screenshot](docs/validation/py_validation_views.png)
</details>

- - -

<details>
<summary>settings.py</summary>

![screenshot](docs/validation/py_validation_settings.png)
</details>

- - -

<details>
<summary>urls.py</summary>

![screenshot](docs/validation/py_validation_urls.png)
</details>

- - -


### Lighthouse

I used [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) to test the performance of the website. 


| Page | Size | Screenshot |
| :----: | :----: | :-----------------------: |
| Home | Desktop | ![screenshot](docs/lighthouse/lighthouse_home_desktop.png) |
| Home | Mobile | ![screenshot](docs/lighthouse/) |
| Sign Up | Desktop | ![screenshot](docs/lighthouse/lighthouse_signup_desktop.png) |
| Sign Up | Mobile | ![screenshot](docs/lighthouse/lighthouse_signup_mobile.png) |
| Sign In | Desktop | ![screenshot](docs/lighthouse/lighthouse_login_desktop.png) |
| Sign In | Mobile | ![screenshot](docs/lighthouse/lighthouse_login_mobile.png) |
| Forgot Password | Desktop | ![screenshot](docs/lighthouse/lighthouse_forgotpassword_desktop.png) |
| Forgot Password | Mobile | ![screenshot](docs/lighthouse/lighthouse_forgotpassword_mobile.png) |
| Add a Thread | Desktop | ![screenshot](docs/lighthouse/lighthouse_addnewthread_desktop.png) |
| Add a Thread | Mobile | ![screenshot](docs/lighthouse/lighthouse_addnewthread_mobile.png) |
| Thread Details | Desktop | ![screenshot](docs/lighthouse/lighthouse_threaddetails_desktop.png) |
| Thread Details | Mobile | ![screenshot](docs/lighthouse/lighthouse_threaddetails_mobile.png) |
| My Profile | Desktop | ![screenshot](docs/lighthouse/lighthouse_myprofile_desktop.png) |
| My Profile | Mobile | ![screenshot](docs/lighthouse/lighthouse_myprofile_mobile.png) |
| Edit Profile | Desktop | ![screenshot](docs/lighthouse/lighthouse_editprofile_desktop.png) |
| Edit Profile | Mobile | ![screenshot](docs/lighthouse/lighthouse_editprofile_mobile.png) |
| My Threads | Desktop | ![screenshot](docs/lighthouse/lighthouse_mythreads_desktop.png) |
| My Threads | Mobile | ![screenshot](docs/lighthouse/lighthouse_mythreads_mobile.png) |
| Edit Threads | Desktop | ![screenshot](docs/lighthouse/lighthouse_editthread_desktop.png) |
| Edit Threads | Mobile | ![screenshot](docs/lighthouse/lighthouse_editthread_mobile.png) |
| Other user's Profile | Desktop | ![screenshot](docs/lighthouse/lighthouse_otherusersprofile_desktop.png) |
| Other user's Profile | Mobile | ![screenshot](docs/lighthouse/lighthouse_otherusersprofile_mobile.png) |
| Search | Desktop | ![screenshot](docs/lighthouse/lighthouse_search_desktop.png) |
| Search | Mobile | ![screenshot](docs/lighthouse/lighthouse_search_mobile.png) |
| Order by | Desktop | ![screenshot](docs/lighthouse/lighthouse_orderby_desktop.png) |
| Order by | Mobile | ![screenshot](docs/lighthouse/) |
| Channels | Desktop | ![screenshot](docs/lighthouse/lighthouse_channels_desktop.png) |
| Channels | Mobile | ![screenshot](docs/lighthouse/lighthouse_channels_mobile.png) |



### Python (Unit Testing)

- To assess the functionality of the application, I utilized Django's built-in unit testing framework.

For test execution, I used the following terminal command:

`python3 manage.py test`

![screenshot](docs/testing/automated_tests.png)




## MANUAL TESTING

### Testing User Stories

Below are user stories I've executed, accompanied by screenshots as evidence.

`First Time Visitors`


<details>
<summary>As a new user I can understand the site's purpose so that I can decide whether or not to sign up
</summary>

![screenshot](docs/testing/landing_page.png)
</details>

- - -

<details>
<summary>As a new user I can sign up and create an account so that I am able to establish my profile and commence using the platform
</summary>

![screenshot](docs/testing/signup_page.png)
</details>

- - -

`Registered/Returning Visitors`


<details>
<summary>As a registered user I can log in to my account so that I can access the site
</summary>

![screenshot](docs/testing/landing_page.png)
</details>

- - -

<details>
<summary>As a registered user I can log out of my account so that I can end my session on my current device
</summary>

![screenshot](docs/lighthouse/)
</details>

- - -

<details>
<summary>As a registered user I can reset my password in case I forget it so that I can get access again to my account
</summary>

![screenshot](docs/testing/reset_password.png)
</details>

- - -

<details>
<summary>As a registered user I can create a profile only by signing up so that I initiate my utilization of the site
</summary>

![screenshot](docs/testing/my_profile.png)
</details>

- - -

<details>
<summary>As a registered user I can change my profile picture so that I am able to enhance my visibility and make it easier for fellow users to recognize me
</summary>

![screenshot](docs/testing/edit_profile.png)
</details>

- - -

<details>
<summary>As a registered user I can update/edit my profile showing my email address and an about me section so that other users can contact me by email or get to know me better
</summary>

![screenshot](docs/testing/edit_profile.png)
</details>

- - -

<details>
<summary>As a registered user I can click on the cancel button while editing my profile so that I can undo the changes I've made and retain my previous profile information
</summary>

![screenshot](docs/testing/edit_profile.png)
</details>

- - -

<details>
<summary>As a registered user, I can view another user's profile so that I can better understand their interests and activities, fostering a more connected and engaging community experience
</summary>

![screenshot](docs/testing/other_users_profile.png)
</details>

- - -

<details>
<summary>As a registered user I can access a dedicated page for my threads so that I can conveniently view and manage all the content I've shared
</summary>

![screenshot](docs/testing/my_threads_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can click on the cancel button while editing a thread so that I can discard the changes I've made and revert to the original thread content
</summary>

![screenshot](docs/testing/edit_thread.png)
</details>

- - -

<details>
<summary>As a registered user I can delete my threads so that I remove content that I no longer wish to be published
</summary>

![screenshot](docs/testing/my_threads_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can add a suggestive image to my thread so that I can suggest what my thread would be about
</summary>

![screenshot](docs/testing/add_new_thread.png)
</details>

- - -

<details>
<summary>As a registered user I can click on a thread so that I can read the full-text
</summary>

![screenshot](docs/testing/thread_details.png)
</details>

- - -

<details>
<summary>As a registered user I can view a list of threads from other people so that I am able to select one to read
</summary>

![screenshot](docs/testing/home_page_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can create new threads so that I share my thoughts
</summary>

![screenshot](docs/testing/add_new_thread.png)
</details>

- - -

<details>
<summary>As a registered user I can see what time and date a thread was created so that I consider reading the whole context depending on its current age
</summary>

![screenshot](docs/testing/home_page_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can click on the cancel button while adding a new thread so that I can abandon the thread creation process and prevent the new thread from being added if I decide not to proceed with it
</summary>

![screenshot](docs/testing/add_new_thread.png)
</details>

- - -

<details>
<summary>As a registered user I can upvote other user's threads so that I let them know I enjoyed their thread
</summary>

![screenshot](docs/testing/thread_details.png)
</details>

- - -

<details>
<summary>As a registered user I can downvote a thread so that I can express dissenting opinions and influence content assessment
</summary>

![screenshot](docs/testing/thread_details.png)
</details>

- - -

<details>
<summary>As a registered user I can view the total number of upvotes on a thread so that I can gauge its popularity and engagement
</summary>

![screenshot](docs/testing/home_page_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can reply on other user's threads so that I engage with the user and open a conversation
</summary>

![screenshot](docs/testing/replies.png)
</details>

- - -

<details>
<summary>As a registered user I can delete my replies so that I can remove what I no longer wish to be published
</summary>

![screenshot](docs/)
</details>

- - -

<details>
<summary>As a registered user I can see the number of replies on a thread so that I know the impact of my thread on other people
</summary>

![screenshot](docs/testing/home_page_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can respond to replies on the communication platform so that I can engage in discussions, share my perspective, and interact with others in the community
</summary>

![screenshot](docs/testing/)
</details>

- - -

<details>
<summary>As a registered user I can utilize existing channels on the communication platform to read, post threads, and engage in conversations so that I can stay informed about diverse topics and contribute my insights and questions
</summary>

![screenshot](docs/testing/channels_expanded_desktop.png)
</details>

- - -

<details>
<summary>As a registered user I can search for other user's threads so that I can discover relevant content
</summary>

![screenshot](docs/testing/search_results.png)
</details>

- - -

<details>
<summary>As a registered user, I can select different sorting options so that I can customize the way I view the list of items and find the information I'm interested in more efficiently
</summary>

![screenshot](docs/testing/order_by_desktop.jpg)
</details>


### MoSCoW prioritization

Listed below are **user stories** that I couldn't successfully implement, designated as "Won't Have" in my ***MoSCoW*** prioritization.


<details>
<summary>As a registered user I can use an emoji button when replying on a thread so that I can describe even better what I want to say
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As a registered user I can receive notifications for replies and upvotes/downvotes on my threads so that I stay updated on interactions and engagement with my content in the communication platform
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As a registered user I can follow other users on the platform so that I stay updated on their activities, threads, and contributions
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As a registered user I can join channels as a member so that I'll get access to discussions, information, and collaboration opportunities within the specific channel
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As a registered user I can create personalized channels on the platform so that I can initiate discussions, share content, and connect with others who share similar interests
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As a registered user I can be assigned roles within a channel so that I can moderate the channel's activities, ensuring smooth discussions, content curation, and maintaining a positive environment for all members
</summary>

![screenshot]N/A
</details>

- - -

`Admin User`

<details>
<summary>As an admin user I can suspend/delete the accounts of users who break the rules of the site so that I can prevent users from constantly violating the guidelines
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As an admin user I can delete other user's threads so that I can update the site's content
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As an admin user I can create a new channel within the communication platform so that users can have a dedicated space to discuss project-related updates, share resources, and collaborate effectively
</summary>

![screenshot]N/A
</details>

- - -

<details>
<summary>As an admin user I can access a dedicated page exclusively meant for administrators so that I can review a list of posts that may require deletion or improved site organization
</summary>

![screenshot]N/A
</details>

- - -


