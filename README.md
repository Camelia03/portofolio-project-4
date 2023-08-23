# GoGlobal



![GoGlobal Website shown on a range of devices]()

GoGlobal stands as a Django-based social media application that enables users to register, generate threads, browse through other user's threads or profile, establish connections with fellow users expressing appreciation through upvotes or downvotes and replies, but also enables to manage their own threads.

[View GoGlobal live](https://go-global-011c0a1d1612.herokuapp.com/)

## CONTENTS

* [User Experience (UX)](#User-Experience-(UX))
  * [Initial Project](#Initial-Project)
  * [User Stories](#User-Stories)

* [Design](#Design)
  * [Color Scheme](#Color-Scheme)
  * [Typography](#Typography)
  * [Wireframes](#Wireframes)
  * [Features](#Features)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

* [Database Design](#Database-Design)
  * [Relationship Diagram](#Relationship-Diagram)
  * [Models](#Models)

* [Agile Development Process](#Agile-Development-Process)
  *[GitHub Projects](#GitHub-Projects)
  *[GitHub Issues](#GitHub-Issues)
  *[Moscow Prioritization](Moscow-Prioritization)



## User Experience (UX)

### Initial-Project

Starting off as a blogging platform, GoGLobal's main goal shifted towards creating a space where users could connect meaningfully. This involved enabling users to share their experiences, ask questions, and engage in threaded conversations. The underlying purpose was to facilitate a sense of staying connected, as encapsulated by the platform's slogan: *stay connected*.

### User Stories


|Epic ID| Epics        | User story ID |    LABELS     |User story                                                                                                      |
|:-----:|:-------------|:----:|:-----------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2 |User authentication|21|Must have|As a new user I can sign up and create an account so that I am able to establish my profile and commence using the platform       |
| 2 |User authentication|22|Must have|As a new user I can understand the site's purpose so that I can decide whether or not to sign up                                  |
| 2 |User authentication|20|Must have|As a registered user I can log in to my account so that I can access the site                                                     |
| 2 |User authentication|19|Must have|As a registered user I can log out of my account so that I can end my session on my current device                                |
| 2 |User authentication|18|Must have|As a registered user I can reset my password in case I forget it so that I can get access again to my account                     |
|24 |User's Profile     |27|Must have|As a registered user I can create a profile only by signing up so that I initiate my utilization of the site                      |
|24 |User's Profile     |26|Must have|As a registered user I can change my profile picture so that I am able to enhance my visibility and make it easier for fellow users to recognize me|
|24 |User's Profile     |28|Could have|As a registered user I can update/edit my profile showing my email address and an about me section so that other users can contact me by email or get to know me better|
|24 |User's Profile     |31|Must have|As a registered user, I can view another user's profile so that I can better understand their interests and activities, fostering a more connected and engaging community experience|
|24 |User's Profile     |35|Should have|As a registered user I can access a dedicated page for my threads so that I can conveniently view and manage all the content I've shared|
|24 |User's Profile     |40|Must have|As a registered user I can click on the cancel button while editing my profile so that I can undo the changes I've made and retain my previous profile information|
|25 |Threads            | 1|Must have|As a registered user I can click on a thread so that I can read the full-text                                                     |
|25 |Threads            | 6|Must have|As a registered user I can add a suggestive image to my thread so that I can suggest what my thread would be about                |
|25 |Threads            |15|Must have|As a registered user I can view a list of threads from other people so that I am able to select one to read                       |
|25 |Threads            |16|Must have|As a registered user I can delete my threads so that I remove content that I no longer wish to be published                       |
|25 |Threads            |17|Must have|As a registered user I can create new threads so that I share my thoughts                                                         |
|25 |Threads            |10|Must have|As a registered user I can see what time and date a thread was created so that I consider the whole context depending on its current age|
|25 |Threads            |39|Must have|As a registered user I can click on the cancel button while editing a thread so that I can discard the changes I've made and revert to the original thread content|
|25 |Threads            |41|Must have|As a registered user I can click on the cancel button while adding a new thread so that I can abandon the thread creation process and prevent the new thread from being added if I decide not to proceed with it|
|42 |Upvote and downvote|11|Must have|As a registered user I can upvote other user's threads so that I let them know I enjoyed their thread                             |
|42 |Upvote and downvote|32|Should have|As a registered user I can downvote a thread so that I can express dissenting opinions and influence content assessment         |
|42 |Upvote and downvote|37|Should have|As a registered user I can view the total number of upvotes on a thread so that I can gauge its popularity and engagement       |
|23 |Replies            |13|Must have|As a registered user I can reply on other user's threads so that I engage with the user and open a conversation                   |
|23 |Replies            |12|Must have|As a registered user I can delete my replies so that I can remove what I no longer wish to be published                           |
|23 |Replies            |4|Should have|As a registered user I can see the number of replies on a thread so that I know the impact of my thread on other people          |
|23 |Replies            |9|Won't have|As a registered user I can respond to replies on the communication platform so that I can engage in discussions, share my perspective, and interact with others in the community|
| 3 |Channels            |34|Could have|As a registered user I can utilize existing channels on the communication platform to read, post threads, and engage in conversations so that I can stay informed about diverse topics and contribute my insights and questions|
|48 |Admin's action      |7|Could have|As an admin user I can suspend/delete the accounts of users who break the rules of the site so that I can prevent users from constantly violating the guidelines|
|48 |Admin's action      |8|Could have|As an admin user I can **delete other user's threads ** so that I can update the site's content                                  |
|48 |Admin's action      |33|Could have|As an admin user I can create a new channel within the communication platform so that users can have a dedicated space to discuss project-related updates, share resources, and collaborate effectively|
|49 |Functionalities     |29|Must have|As a registered user I can search for other user's threads so that I can discover relevant content                               |
|49 |Functionalities     |30|Must have|As a registered user, I can select different sorting options so that I can customize the way I view the list of items and find the information I'm interested in more efficiently|
|23 |Replies             |5|Won't have|As a registered user I can use an emoji button when replying on a thread so that I can describe even better what I want to say   |
|49 |Functionalities     |43|Won't have|As a registered user I can receive notifications for replies and upvotes/downvotes on my threads so that I stay updated on interactions and engagement with my content in the communication platform|
|49 |Functionalities     |44|Won't have|As a registered user I can follow other users on the platform so that I stay updated on their activities, threads, and contributions|
| 3 |Channels            |45|Won't have|As a registered user I can join channels as a member so that I'll get access to discussions, information, and collaboration opportunities within the specific channel|
| 3 |Channels            |46|Won't have|As a registered user I can create personalized channels on the platform so that I can initiate discussions, share content, and connect with others who share similar interests|
| 3 | Channels           |47|Won't have|As a registered user I can be assigned roles within a channel so that I can moderate the channel's activities, ensuring smooth discussions, content curation, and maintaining a positive environment for all members|


### Color Scheme

- `#E58C18` used as a primary color for buttons.
- `#eca446` used for hovering primary-colored buttons.
- `#004696` used as a secondary color for buttons, for navigation and footer, but also for small details such as: signup/login links, edit thread button, and total number of threads in a channel.
- `#d2e4f9` used for hovering secondary colored buttons.
- `#f9f9f9` used for cards as a background-color.
- `#f9b1b1` used for the delete button.
- `#f8dddd` used for hover the delete button.

GoGlobal combines a range of colors that balance cool and warm tones, evoking a sense of harmony and diversity. 

The whites and light blues contribute to a fresh and airy feel, while the darker navy blue and the pop of orange add depth and visual interest. The light gray acts as a bridge, offering a subtle transition between the more vibrant and muted colors.


![GoGlobal Color Palette](/static/media/goglobal_color_palette.png)
The colour palette was created using the [Coolors](https://coolors.co/) website.



![GoGlobal's logo Color Pallete](/static/media/logo_palette.pngpng)
The logo was created using the [LOGO](https://app.logo.com/) website.

### Typography

Google Fonts was used for the following fonts:

* Black Ops One is used for the logo of GoGlobal. It is sans-serif font.
* Lato is used for the body text on the website. It is a sans-serif font. 

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer, upvote and downvote button, replies and channels.



### Wireframes

I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes for mobile and desktop.


### Sign In Page

<details>
<summary>View Sign In Page</summary>

#### Desktop
![screenshot](docs/wireframes/LogIn%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/LogIn%20mobile%20version.png)

</details>

### Sign Up Page

<details>
<summary>View Sign Up Page</summary>

#### Desktop
![screenshot](docs/wireframes/Sign%20Up%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Sign%20Up%20mobile%20version%20.png)

</details>

### All threads Page

<details>
<summary>View All threads Page</summary>

#### Desktop
![screenshot](docs/wireframes/All%20threads%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/All%20threads%20mobile%20version.png)

</details>

### Channels Page

<details>
<summary>View Channels Page</summary>

#### Desktop
![screenshot](docs/wireframes/Channels%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Channels%20mobile%20version.png)

</details>

### Add a new Thread Page

<details>
<summary>View Add a new Thread Page</summary>

#### Desktop
![screenshot](docs/wireframes/Add%20a%20new%20thread%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Add%20a%20new%20thread%20mobile%20version.png)

</details>

### Edit Thread Page

<details>
<summary>View Edit thread Page</summary>

#### Desktop
![screenshot](docs/wireframes/Edit%20your%20thread%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Edit%20your%20thread%20mobile%20version.png)

</details>


### My threads Page

<details>
<summary>View My threads Page</summary>

#### Desktop
![screenshot](docs/wireframes/My%20threads%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/My%20threads%20mobile%20version.png)

</details>

### Other user's profile Page

<details>
<summary>View Other user's profile Page</summary>

#### Desktop
![screenshot](docs/wireframes/Other%20user's%20profile%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Other%20user's%20profile%20mobile%20version.png)

</details>

### Search Threads Page

<details>
<summary>View Search Threads Page</summary>

#### Desktop
![screenshot](docs/wireframes/Search%20threads%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Search%20threads%20mobile%20version.png)

</details>

### Thread Details Page

<details>
<summary>View Thread Details Page</summary>

#### Desktop
![screenshot](docs/wireframes/Thread%20details%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/Thread%20details%20mobile%20version.png)

</details>


### My Profile Page

<details>
<summary>View My Profile Page</summary>

#### Desktop
![screenshot](docs/wireframes/User%20profile%20Desktop%20version.png)

#### Mobile
![screenshot](docs/wireframes/User%20profile%20mobile%20version.png)

</details>


### Features

### Existing Features

- **Header and Navigation**

    - The navigation bar features a logo, the page's name, and links tailored for both unauthenticated and authenticated users. 
        - The nav bar contains everything the user will need to navigate the site. The site logo always appears on the site menu with the other items only showing for logged in users. 

        - For the unauthenticated users, the navbar only shows the authentication pages(Register, Login and Home-which brings them back to the landing page).

        - For authenticated users, the nav bar hides the authentication pages and shows only a search bar, a dropdown menu for user's profile and the logo. From the dropdown menu for user's profile, the user can go to their profile page(for editing their profile), to their threads(for editing or delete their threads) or to simply log out.

- **Default navbar for unregistered user**

    ![screenshot](docs/testing/nav_unreg_user.png)

- **Navbar for registered user**

    ![screenshot](docs/testing/nav_reg_user.png)

- **Navbar on mobile**

    ![screenshot](docs/testing/mobile_nav.png)

- **Navbar expanded on mobile**

    ![screenshot](docs/testing/nav_channels_expanded_mobile.png)

- **Navbar expanded dropdown menu**

    ![screenshot](docs/testing/nav_expanded_dropdown_mobile.png)


- **Landing or Log In Page**

    - This page is where users arrive when they first visit the site or before they log in if they don't have an active session. It greets them and provides the choice to either create a new account or access an existing one.

      - Also here, users with accounts can log in using their username or email and password.
      - The page also provides a sign-up link for those looking to create an account. 
      - If a user forgets their password, there's a link to reset it.

    ![screenshot](docs/testing/landing_page.png)


- **Sign Up Page**

    - This is where users can set up an account by inputting their email, preferred username, and password (repeated for confirmation). If users arrive here unintentionally, instead of the login page, they can find their way to the appropriate page through the provided link.

    ![screenshot](docs/testing/signup_page.png)

- **Reset Password**

    - Users who forget their password can initiate a reset by entering the email they used for signing up. An email will be sent containing a link to establish a new password.

    ![screenshot](docs/testing/forgot_password_confirmation.png)

    ![screenshot](docs/testing/forgot_password_confirmation.png)

    ![screenshot](docs/testing/password_reset.png)

    ![screenshot](docs/testing/password_reset_confirmation.png)

- **Footer**

    - The footer appears across the website and includes information about me as the developer with links to social media and GitHub pages. This lets the user get to know me as the developer and connect on these platforms if they wish.

    ![screenshot](docs/testing/footer.png)

- **Add Thread Form**

    - This is the space where users can generate their threads. It is accessible on both the home page and when selecting a channel from the sidebar. It requires you to choose a channel where you wish your thread to be, provide a title, write your content, and optionally include an image to better convey your message.

    ![screenshot](docs/testing/add_new_thread.png)

- **Channels**

    - This is the space where users can explore the channels feature, present on both the home page(for mobile) and the sidebar when navigating. It invites users to select a channel that best matches their discussion topic. This categorization enhances content organization and focuses discussions. Whether initiating a thread from the home page or within a selected channel, this feature ensures a smooth user experience, promoting relevant and engaging interactions.

  - **Channels-sidebar-desktop**
    ![screenshot](docs/testing/home_page_desktop.png)

  - **Channels-homepage-mobile**
    ![screenshot](docs/testing/home_page_mobile.png)

  - **Channels-expanded-desktop**
    ![screenshot](docs/testing/channels_expanded_desktop.png)

  - **Channels-expanded-mobile**
    ![screenshot](docs/testing/channels_expanded_mobile.png)

- **Order by**

    - This is where users can customize content organization on the home page and channels page. The "Order By" menu empowers users to personalize how content is displayed, ensuring a tailored browsing experience.
    
  - **Order-by-desktop**
    ![screenshot](docs/testing/order_by_desktop.jpg)

  - **Order-by-mobile**
    ![screenshot](docs/testing/order_by_mobile.jpg)

- **Pagination**

    - The pagination feature divides content into manageable segments of 5 items per page. This design ensures smoother navigation through extensive content, providing users with a more focused and comprehensible browsing experience.
    
    ![screenshot](docs/testing/pagination.png)

- **Home Page**

    - Central to the site are user threads, showcased on the home page. Users can explore threads, choose channels, sort, and search. Essential thread data like reply count, upvotes, and downvotes are displayed under the "Read more" button for quick insights.

  - **Home Page-desktop**
    ![screenshot](docs/testing/home_page_desktop.png)

  - **Home Page mobile**
    ![screenshot](docs/testing/home_page_mobile.png)

- **My Profile Page**

    - My profile page presents a warm welcome message upon entry, along with the user's email address prominently displayed. Additionally, an "About Me" section offers insights about user's persona. To facilitate personalization, an "Edit Profile" button grants the authenticated user control over their displayed information.

    ![screenshot](docs/testing/my_profile.png)

- **Edit Profile**

    - The "Edit Profile" section provides a comprehensive form for users. It features fields for updating the username, selecting or modifying the profile image, and editing the "About Me" section. Users have the options to save their changes or cancel the process, conveniently accessible through corresponding buttons. Once changes are submitted, a success message confirms the successful update.

    ![screenshot](docs/testing/edit_profile.png)

- **My threads Page**

    - The "My Threads" page offers users a consolidated view of all their threads. This page showcases relevant buttons such as "Read More," "Edit Thread," and "Delete Thread" for each entry. These buttons empower users to access the complete thread content, make edits, or remove threads as needed.

    ![screenshot](docs/testing/my_threads_desktop.png)

- **Read more/ Thread Details**

    - The "Read More" button directs users to the thread details page, offering an immersive experience. Here, users encounter the entire post, enriched with context. The channel to which it belongs, its title, creation timestamp, author's name, and profile picture contribute to the comprehensive view. Additionally, the thread's associated image, content, but also the counted upvotes, and downvotes are prominently displayed.
    - To encourage engagement, a dedicated section enables users to leave a reply, fostering dynamic discussions.Following this, a "Replies" section presents the users's names and their replies, creating a comprehensive space for discussions. 

 - **Read more/ Thread Details Page**
    ![screenshot](docs/testing/thread_details.png)

  - **Thread Details Page- replies section**
    ![screenshot](docs/testing/replies.png)


- **Edit Thread Page**

    - "Edit Thread" presents a form for modifying threads. Users can choose a new channel, change the title, content, and image. The options to save or cancel changes are presented through buttons. Upon submitting changes, a success message confirms the update's completion.

    ![screenshot](docs/testing/edit_thread.png)

- **Delete Thread**

    - Users can delete their threads by clicking the delete button. A confirmation window appears to prevent accidental deletions. If users change their minds, a button takes them back to the post. For thread deletions, a successful action message is displayed after the process is completed.

    ![screenshot](docs/testing/delete_thread.png)

- **Replies**

    - Replies appear beneath threads. The replies authors and threads authors have the ability to delete their replies, while replies authors can edit their replies as well. 

    ![screenshot](docs/testing/replies.png)


- **Edit reply**

    - Reply authors can edit their replies. Clicking the edit icon takes them to a page where they can make changes and save. If they edit by mistake, a button brings them back to the post.

    ![screenshot]()


- **Delete reply**

    - The replies can be deleted by both the reply's author or the thread's author using the delete icon. To prevent accidental deletions, a confirmation page appears. Users can return to the thread they replied on using a button if they change their mind about deleting the reply.

    ![screenshot]()

- **Other user's Profile**

    - Clicking the thread author's name reveals their profile. This page shows their name, email, and "About Me" section for better communication. You can also view their threads with full details on their profile.

    ![screenshot](docs/testing/other_users_profile.png)


- **Search**

    - The search bar empowers users to quickly find what they're looking for. It allows users to enter keywords or phrases, and it expertly guides them to threads that match their interests. Even if no results are found for a specific keyword, the search bar ensures the user informed, allowing them to refine their search or explore other topics.

    ![screenshot](docs/testing/search_results.png)
    ![screenshot](docs/testing/no_search_results.png)


- **Logout**

    - To conclude their session and log out, users can do so conveniently from the My Profile dropdown menu. When the logout button is clicked, a confirmation page appears, ensuring the user's intention. Upon confirming, clicking the confirmation button redirects users to the landing page, accompanied by a confirmation message that acknowledges their successful logout.

    ![screenshot]()


- **Admin Panel**

    - The admin panel is exclusively accessible via Django's backend by adding "/admin" to the end of the website's URL. Admins hold the authority to determine whether a post should be deleted.

    ![screenshot]()


- **Error Pages**

    - If a user reaches a page that doesn't exist or isn't allowed (like a regular user trying to access the admin panel or deleting others' posts), they'll see an error page. It has a button to take them back to their feed.

    ![screenshot]()

    ![screenshot]()

    ![screenshot]()


### Future Features

- Reply to a reply
    - Registered users will have the ability to respond to replies on the communication platform. This empowers them to actively participate in discussions, express their viewpoints, and engage with others within the community.

- Delete threads and replies as an admin
    - Admin will have the authority to delete threads and replies authored by other users. This capability enables them to manage and update the site's content effectively.

- Emoji button
    - Registered users will be able to utilize an emoji button while replying to threads. This allows them to convey their thoughts more vividly and accurately.

- Notifications
    - Registered users will be able to receive notifications for replies, upvotes, and downvotes on their threads. This keeps them informed about interactions and engagement with their content within the communication platform.

- Follow other users
    - Registered users will have the option to follow other users on the platform. This ensures they receive updates about their activities, threads, and contributions.

- Join channels as a member
    - Registered users will have the ability to join channels as members. This grants them access to discussions, information, and opportunities for collaboration within the chosen channel.

- Roles within a channel
    - Registered users will have the capability to be assigned specific roles within a channel. This feature empowers users to take on moderation responsibilities, ensuring the channel's activities run smoothly. 

- Allow users to create their own channels
    - Registered users will be able to create personalized channels on the platform. This enables them to start discussions, share content, and connect with like-minded individuals who have similar interests.



## Technologies-Used

### Languages-Used

 - HTML is utilized as the primary language to establish the website's structural framework.
 - CSS is employed to tailor the visual style of the website.
 - JavaScript is leveraged for modifying the DOM across different pages.
 - Python plays a pivotal role in configuring the site's fundamental functionalities, including models and views.

### Frameworks,-Libraries-&-Programs-Used:
- Python Modules/Packages-Used:

This project relies on several core packages, with some key ones highlighted along with their functions:

 - django: A high-level Python web framework used for developing this application/site.
 - crispy-bootstrap4: A Bootstrap 4 template pack designed for django-crispy-forms.
 - dj3-cloudinary-storage: This package simplifies integration with Cloudinary by implementing Django Storage API.
 - django-allauth: An integrated set of Django applications designed for authentication, registration, account management, and third-party (social) account authentication.
 - django-crispy-forms: Offers a crispy filter and `{% crispy %}` tag for elegant and DRY (Don't Repeat Yourself) rendering of Django forms.
 - psycopg2: An adapter for the Python programming language that facilitates interaction with PostgreSQL databases.
 - coverage: This package generates a coverage report for automated testing, aiding in testing effectiveness assessment.

- Frameworks & Tools

Here's a rundown of the key tools and platforms utilized in this project:

 - Django: Employed for establishing the website's backend logic and user model.
 - Bootstrap: Woven into the site's fabric, it contributes to responsiveness, layout, and predefined style elements.
 - CodeAnywhere: Utilized for coding and development tasks, including writing, committing, and pushing code to GitHub.
 - GitHub: Serves as the host for the website's source code. It also records the Agile development framework implementation, incorporating issues, milestones, and projects.
 - ElephantSQL: Used as the Postgres database.
 - Heroku: Used for deploying the live version of the website.
 - Cloudinary: Acts as a cloud storage solution for website media and static files. It also offers media manipulation and optimization features.
 - Balsamiq: Chosen for creating project wireframes.
 - Gmail: used to create an email address to send password reset emails from.
 - Google Dev Tools - to troubleshoot and test features, solve issues with responsiveness and styling.
 - [Am I Responsive?](http://ami.responsivedesign.is/) - to show the website image on a range of devices.
 - Google Fonts: Imports fonts to enhance the website's typography.
 - Font Awesome: Provides the necessary icons across the site.
 - LOGO: Provides the necessary official logo across the site.
 - Coolors: Provides the color palette across the site.

## Database Design
By creating an entity relationship diagram, I gained a clear picture of how my data structures interconnect. This approach greatly facilitated the development process by providing a consolidated reference point, sparing me the need to navigate through individual models.py files for guidance.

### Relationship Diagram

![screenshot](docs/database_diagram.jpg)

To create the databse diagram, I used [PyCharm](https://www.jetbrains.com/pycharm/) which helped me generate it automatically.

 ### Models

The following are the models created for GoGlobal.

- **Allauth User Model**
    - The User model was built using [Django's Allauth library](https://django-allauth.readthedocs.io/en/latest/overview.html)
    - When a user is created, they're automatically assigned a profile through the Profile model.

- **Profile**

    | **Field** | Type | Notes |
    | --------- | ---- | ----- |
    |  id | Integer | PK |
    | user | OneToOne | FK to **User** model |
    | about | TextField | |
    | avatar | CloudinaryField | |


- **Thread**

    | **Field** | Type | Notes |
    | --------- | ---- | ----- |
    |  id    | Integer | PK |
    | user | ForeignKey | FK to **User** model |
    | title | CharField |  |
    | content | TextField | |
    | created_on | DateTimeField | |
    | image | CloudinaryField | |
    | edited_on | DateTimeField | |
    | channels | ForeignKey | FK to **Channel** model |


- **Reply**

    | **Field** | Type | Notes |
    | --------- | ---- | ----- |
    |  id    | Integer | PK |
    | thread | ForeignKey | FK to **Thread** model |
    | user | ForeignKey   | FK to **User** model   |
    | content | TextField | 
    | created_on | DateTimeField |  


- **Upvote**

    | **Field** | Type | Notes |
    | --------- | ---- | ----- | 
    |  id    | Integer | PK |
    | thread | ForeignKey | FK to **Thread** model |
    | user | ForeignKey   | FK to **User** model   |
    | created_on | DateTimeField |  

    - unique constraint on **thread** and **user**


- **Downvote**

    | **Field** | Type | Notes |
    | --------- | ---- | ----- |
    |  id    | Integer | PK | 
    | thread | ForeignKey | FK to **Thread** model |
    | user | ForeignKey   | FK to **User** model   |
    | created_on | DateTimeField |  

    - unique constraint on **thread** and **user**


- **Channels**

    | **Field** | Type | Notes |
    | --------- | ---- | ----- |
    |  id    | Integer | PK |
    | name | CharField |  
    | image | CloudinaryField | 
    | icon | CharField |  
    | slug | SlugField |  


## Agile Development Process

### GitHub Projects
 The project's development was coordinated using GitHub's issues, milestones, and projects features. [GitHub Projects](https://github.com/Camelia03/portofolio-project-4/projects) served as an Agile tool, adapted effectively with appropriate tags and issue assignments.


This approach utilized user stories and a basic Kanban board. It helped me manage tasks, track progress, and smoothly move through development, testing, and completion phases.

![screenshot](docs/goglobal_project_board.png)

### GitHub Issues

GitHub Issues served as an additional Agile tool. Within this context, I utilized my own User Story Template to manage user stories. To enhance issue organization and streamline workflows, I created an "EPIC" tag for effectively categorizing and addressing issues on the site.

- [Epics](https://github.com/users/Camelia03/projects/6/views/2)
    ![screenshot](docs/epics_board.png)

- [Open Issues](https://github.com/Camelia03/portofolio-project-4/issues)

    ![screenshot](docs/open_issues.png)

- [Closed Issues](https://github.com/Camelia03/portofolio-project-4/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](docs/closed_issues.png)


### MoSCoW Prioritization

This technique proves valuable for my project helping me to prioritize product features.
Before implementing my Epics, I broke them down into individual stories.
By following this method, I could then apply MoSCoW prioritization and labels for my user stories directly in the Issues tab.


|                  |       |      |      |
| ---------------- | ----- | ---- | ---- |
|  **Must Have** | *max 60% of stories* | guaranteed to be delivered | These are the core features that are vital for the initial release.|
|  **Should Have** | *aprox.20% of stories* | adds significant value, but not vital | These features are important and should be prioritized, but the project can proceed without them.|
|  **Could Have** | *20% of stories* | has small impact if left out | These features provide added value and are desirable, but they are not essential for the current release.|
|  **Won't Have** |  | not a priority | These are features that have been deliberately deferred to a later phase or release.|