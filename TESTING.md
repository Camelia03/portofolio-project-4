# Testing

Return back to the [README.md](README.md) file.

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [Jigsaw Validator](#Jigsaw-Validator)
  * [JavaScript Validator](#JS-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)



- - -

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

![screenshot](docs/validation)
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