# An Seo

Return to Read Me Document [here](README.md)
## Contents
- [Testing Round 1](#testing-round-1)
- [Error 403](#error-403)
  - [Current Status](#current-status)
- [Testing Round 2](#testing-round-2)

<br>


## Manual Testing
<span style="color:#56a832; font-weight:bold; font-size:20px">Testing of USER STORIES</span>

<p>I carried out manual testing as follows, incorporating USER STORIES and ISSUES from the Agile Kanban.</p>

[Kanban Board](https://github.com/TNolan01/player_track/projects/1)

<br>

## Testing Round 1

<p align="center" width="100%"> 
<img src="media/testing/Test1.png" alt="test image 1" width=""/>
</p>
 
<p align="center" width="100%"> 
<img src="media/testing/Test2.png" alt="test image 2" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test3.png" alt="test image 3" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test4.png" alt="test image 4" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test5.png" alt="test image 5" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test6.png" alt="test image 6" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/duplicate_player.png" alt="test image 6" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test7.png" alt="test image 7" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test8.png" alt="test image 8" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test9.png" alt="test image 9" width=""/>
</p>

[Back to content](#contents)

## Error 403

<span style="color:#56a832; font-weight:bold; font-size:16px">HTTP vs. HTTPS Issue</span>

<span style="color:#ebd80c; font-weight:bold; font-size:14px">Test Case No.9</span>

<p>During the testing I discovered that when I entered the name of the application into the Microsoft Edge browser as <span style="color:orange; font-weight:bold;">'an-seo.herokuapp.com'</span> without prefacing it with 'http:// or https://' then the application was opening as http://an-seo.herokuapp.com in the Edge browser. The Login screen was rendering correctly but if any user attempted login the application would get a 403 Error relating to CSRF issue as soon as the user clicked the Login button.</p>
<p>I initially thought this was a Microsoft Edge issue. Without being prefaced with https://, Edge defaulted to http:// protocol. If I entered the entered the site as https:// there would be no login issues. Possibly a security issue or setting on the Edge browser?, not a browser that I use.</p>

<p>Having checked further I found that if I used http:// on Google Chrome I was able to replicate the 403 error and so the issue was not unique to Microsoft Edge.</p>

<span style="color:#ebd80c; font-weight:bold; font-size:14px">Initial Fix.</span>

<p>I checked code and found all csrf_token's were located correctly in the relevant forms and I could see not issues in the views.py. My initial fix to the issue was to create a custom 403 page.</p>

<p>When triggered by a 403 Error the custom 403 page would revert the user back to a secure HTTPS connection, https://an-seo.herokuapp.com, and the application would be fully functional from that point.</p>



<span style="color:#ebd80c; font-weight:bold; font-size:14px;">Further Investigation Of Issue.</span>

- Investigation of similiar issues suggested adding CSRF specific settings in the settings.py But of these related to Django 4+ and not Django 3 as I am using. Having experimented with these settings I found that they had no impact on the issue.    
- Opening the Login Page through Google's Developer Tools showed that the form had created a CSRF token.

<p align="center" width="100%"> 
<img src="media/testing/cookie.png" alt="dev tools shot" width=""/>
</p>
<br>

- Potential solutions suggested using a decorator, <span style="color:blue; font-weight:bold;">@csrf_exempt</span> on particular views to bypass the issue. I also found information about changing <span style="color:blue; font-weight:bold;">SESSION_COOKIE_SECURE</span> and <span style="color:blue; font-weight:bold;">CSRF_COOKIE_SECURE</span> in the settings.py. 
Neither of these settings were in the Code Institute template and so I did not see the advantage of adding them just to set them to FALSE and weaken the security of a CSRF token.

<p align="center" width="100%"> 
<img src="media/testing/cookies.png" alt="csrf settings" width=""/>
</p>
<br>

- Opening Developer Tools in the Microsoft Edge browser and carrying out further testing the error shown was <span style="color:blue; font-weight:bold;">Cross-Origin Read Blocking (CORB)</span>

<p align="center" width="100%"> 
<img src="media/testing/favicon.png" alt="csrf settings" width=""/>
</p>
<br>

This error was indicating the issue was with <span style="color:blue; font-weight:bold;"> favicon.ico</span>
At this point of testing I was not using Favicon or had no reference to it in my code.

Further testing by connecting to my application through the HTTP protocol and the HTTPS protocol and checking showed that on HTTP, Favicon.ico was not creating a CSRF Token but when connecting through HTTPS it was generating a CSRF token. I do not know enough about the browsers request for a Favicon logo.

I generated a Favicon logo, uploading the image file to Cloudinary, as static storage, and referenced the file in the header of my main.html but this didnt clear the issue.

<span style="color:#56a832; font-weight:bold; font-size:14px;">HTTP Protocol<span>

<p align="center" width="100%"> 
<img src="media/testing/favicon_on_http.png" alt="csrf http" width=""/>
</p>
<br>

<span style="color:#edb80c; font-weight:bold; font-size:14px;">HTTPS Protocol<span>

<p align="center" width="100%"> 
<img src="media/testing/favicon_on_https.png" alt="csrf https" width=""/>
</p>
<br>

### Current Status
<span style="color:#56a832; font-weight:bold; font-size:14px;">Current Status of Error</span>
<p>The issue still exists but my initial fix of custom 403 page is the work around if a user encounters the problem.</p>
<p>I cannot find any further information on this issue in relation to Favicon but I will return to it after further function testing.</p>


[Back to content](#contents)


## Testing Round 2

<p align="center" width="100%"> 
<img src="media/testing/Test10.png" alt="test image 10" width=""/>
</p>
<br>

<p align="center" width="100%"> 
<img src="media/testing/Test11.png" alt="test image 11" width=""/>
</p>
<br>

<p align="center" width="100%"> 
<img src="media/testing/Test11_image.png" alt="Test11_image" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test12.png" alt="test image 12" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test13.png" alt="test image 13" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/messages.png" alt="messages" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test12_image.png" alt="messages" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test14.png" alt="test image 14" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/validate_player.png" alt="validate player" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test15.png" alt="test image 15" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/blank_team_sheet.png" alt="blank team" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test16.png" alt="test image 16" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/team_sheet.png" alt="team sheet" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test17.png" alt="test image 17" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/blank_login.png" alt="blank login" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test18.png" alt="test image 18" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/403_error.png" alt="403 error" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test19.png" alt="test image 19" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/test19_image.png" alt="test image 19" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/404_error.png" alt="404 error" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test20.png" alt="test image 20" width=""/>
</p>

<p>Screen shot show existing match fixtures prior to test.</p>

<p align="center" width="100%"> 
<img src="media/testing/match_screen.png" alt="match fixtures" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/game_date_duplication.png" alt="game duplication" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test21.png" alt="test image 21" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/game_date_past.png" alt="game duplication" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test22.png" alt="test image 22" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/incorrect_password.png" alt="incorrect password" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/Test23.png" alt="test image 23" width=""/>
</p>

<p align="center" width="100%"> 
<img src="media/testing/account_sucess.png" alt="account success" width=""/>
</p>