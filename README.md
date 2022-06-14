# Anseo
​
[Anseo](link-to-website) is a web based application which allows managers and coaches of to track the attendance of their players at training and for matches. The application is primarily designed for underage and amateur sports. 
​
![Site display on different screens](am-i-responsive-image)
​
---
​
## Contents
​
- [Anseo](#gift-of-giving)
  - [Contents](#contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [Site Visitor/User Goals](#site-visitoruser-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
      - [**Requirements**](#requirements)
      - [**Expectations**](#expectations)
    - [Design Choices](#design-choices)
      - [**Fonts**](#fonts)
      - [**Colours**](#colours)
  - [Wireframes](#wireframes)
    - [**Site Layout**](#site-layout)
  - [Information Architecture](#information-architecture)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries & Frameworks](#libraries--frameworks)
    - [Tools](#tools)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
    - [Redundant features](#redundant-features)
  - [Changes applied since planning](#changes-applied-since-planning)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Deployment to Github](#deployment-to-)
  - [Credits](#credits)
    - [Images](#images)
    - [Image editing](#image-editing)
    - [Code ideas](#code-ideas)
  - [Acknowledgements](#acknowledgements)
​
---
​
## UX
​
### Project Goals
​
The main goal of this project is to provide coaches of underage teams the ability to track the attendance of the players at training sessions. This data then gives the user a simple visual guide as to which players are regularly participating and so aid the coach/manager in portioning game time when it comes to competitive games and matches.
​
### Site Owner Goals
​
- Provide the users with a simple system, availiable to use via mobile devices.
​
### Site Visitor/User Goals
​
- Site visitors will have the ability to view the details of upcoming training sessions and match fixtures. The typical site visitor will be a parent or guardian of a child who is part of the team or a member of a team itself.
<br>
- Site users will have the ability to...
    
    <ul>
    <li>Create, Update and Delete Players.</li>
    <li>Create, Update and Delete Training Sessions.</li>
    <li>Create, Update and Delete Matches.</li>
    <li>View player attendance histories.</li>
    <li>View records of training sessions.</li>
    <li>View records of team selections.</li>
    </ul>

​
### User Stories
​
**Applies to all site users:**
​
- As a user, I am able to...view upcoming training sessions and matches.
<!--  
​
**Applies to new site users:**
​
- As a user, I am able to 
​
**Applies to all returning users:**
​
- As a user, I am able to  -->
​
**Applies to a superuser (site owner):**
​
- As a user, I am able to...
​<br>
[Back to content](#contents)
​
### User Requirements and Expectations
​
#### **Requirements**
​
- Visually pleasant app design
- Easy site navigation
- Information of the content layed out in a simple and clear way on both mobile and larger screens
- Self-explanatory icons where text is absent
​
#### **Expectations**
​
- Quick app load time.
- Easy to use interface.

​<br>
[Back to content](#contents)
​
### Design Choices
​
#### **Fonts**
​
- *All fonts*
​
  ```font-family: Baloo Bhaijaan 2', sans-serif;```
​
- *Special font - logo*
​
  ```font-family: ''Meow Script', cursive;```
​
#### **Colours**
​
![Colour palette](colour-pallette-img)
​
[Back to content](#contents)
​
## Wireframes
​
### **Site Layout**
​
Site moc-ups were designed using [figma](figma). The focus was on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as mobile, tablet and larger screens.
​
You can view the wireframes created for this project in [site wireframes](/docs/wireframes.pdf) folder.
​
  **Please note, as we were developing the project, we have identified some weaknesses in the UX and therefore made the required changes. The deployed site looks somewhat different in comparison to the wireframes. These changes will allow the user to have a better experience and allow easier navigation. The design theme of the features is a close match to the overall site to ensure continuation and flow.*
​
[Back to content](#contents)
​
---
​
## Information Architecture
​
​
[Back to content](#contents)
​
---  
​
## Technologies
​
### Languages
​
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
​
### Libraries & Frameworks
​
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google fonts](https://fonts.google.com/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
​
### Tools
​
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
<!-- - [Visual Studio Code](https://code.visualstudio.com/)
- [Color editor](https://coolors.co/)
- [Favicons](https://fontawesome.com/icons?d=gallery)
​ -->
[Back to content](#contents)
​
---
​
## Features
​
The appliaction is uses a PostgreSQL database which contains the purpose designed models.
​
The site uses the Django and Bootstrap 

### Implemented Features
​
- The site has **responsive design** when viewed on a mobile, tablet, and desktop.
- **Easy navigation** to external sites, such as social media accounts.
- The user is given feedback when they interact with the website (i.e. login to the website, add new gift, commit to buying a gift etc).
​
[Back to content](#contents)
​
---
​
## Changes applied since planning
​
---
​
## Testing
​
## Functional Testing
​
TC001 
​
**Description**
​
Test something.
​
**Steps**
​
- Navigate to https://website
- 
​
**Expected**
​
This happened
​
**Actual**
​
This happened
​
![TC001](img-of-test)
​
<hr>
​
TC002
​
​
## Validator Testing
​
### CSS
​
Base Css
​
![Base CSS](docs/testing/base_css.JPG)
​
### JavaScript
​
Base JS
​
![Base JS](docs/testing/base_js.JPG)
​
### HTML
​
The following Validated with no errors:
- Home Page
- 
​
![Success](docs/testing/html_validator.JPG)
​
The Following Validator with the same error:
- The something page
​
![Error](docs/testing/edit_gift_add.JPG)
​
​
[Back to content](#contents)
​
---
​
## Deployment
​
### Deployment:
<br>

Deployment of this project is carried out with  Heroku, https://www.heroku.com . The deployment procedure is a follows.  
<ol>
<li>Log in to Heroku, creating a new account if you are not a current user.</li>
<li>Click on the 'New' button in the top right corner and from the drop-down menu select 'Create new app'.</li>
<li>Create an App name and select your Region from menu.</li>
<li>Click the 'Create App' button.</li>
<li>You will now have a menu for your new app. From here click on the Settings Tab and in the Config Vars. Click Reveal Config Vars.</li>
<br>
<p align ="center">
<img title="heroku" alt="screen shot of Heroku app menu" src="images/readme_images/heroku_app_menu.png"></p>
<br>

<li>You need to create Config Vars for the Google API Credentials. Enter 'CREDS' as the KEY and then copy the entire contents of the creds.json file from GITPOD in the VALUE section, click the Add button to finish.  </li>
<li>A second Config Vars will be required. In the KEY box enter 'PORT' and in the VALUE box enter 8000 and then click the Add button.</li>
<li>Scroll down to the Buildpacks section. Click Add buildpack. From the menu select Python and click Save Changes. </li>
<li>Click Add buildpack again and Node.js. The Buildpacks must added in this order. If not, you can click on the packs and drag them to the correct order as shown in the image.</li>
<br>
<p align ="center">
<img title="heroku" alt="screen shot of Heroku settings" src="images/readme_images/heroku.png"></p>
<br>
<li>Return to menu at the top of the page and click on Deploy. Select Github as the deployment method.</li>
<li>Confirm you want to connect to GitHub using your account credentials for Git. Once Heroku has access search for the relevant repository name and click the connect button.</li>
<li>At the bottom of the deploy page select the preferred deployment type. You can use Manual Deploy which will deploy based on the current state of the selected Git branch. You can also Enable Automatic Deploys for automatic deployment when you push updates to Github selected branch.</li>
<br>

[Back to Contents](#contents) 
<br>

### Cloning:

[Click here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

1. Log in to GitHub and locate the [GitHub Repository] https://github.com/TNolan01/player_track
2. Under the repository name, click "Code".
3. To clone the repository using HTTPS. Under "HTTPS" copy the link.
4. Go to your local terminal with git installed
5. Change the current working directory to the location where you want the cloned directory to be created/located.
6. Type `git clone` and then you paste in the URL you copied in Step 3.

  ```
  $ git clone https://github.com/TNolan01/player_track
  ```

7. Press Enter. Your local clone will be created.
<br>

[Back to Contents](#contents) 
<br>
​
---
​
## Credits
​
### Images
​
* 
​
### Image editing
​
* 
​
### Code ideas
​
* 
​
[Back to content](#contents)
​
---
​
## Acknowledgements
​
Site creators:
​

​
[Back to content](#contents)