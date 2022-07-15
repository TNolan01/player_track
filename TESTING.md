# An Seo

## Manual Testing
### Testing Phase 1 

<p>I carried out manual testing as follows:</p>
 

<p align="center" width="100%"> 
<img src="media/read_me/multi_screen.png" alt="screen shots of site" width=""/>
</p>


<span style="color:#56a832; font-weight:bold; font-size:16px">HTTP vs. HTTPS Issue</span>
<p>During the testing I had discovered that when I entered the name of the application into the Microsoft Edge browser as <span style="color:orange; font-weight:bold;">'an-seo.herokuapp.com'</span> without prefacing it with 'http:// or https://' then the application was opening as http://an-seo.herokuapp.com in the Edge browser. The Login screen was rendering correctly but if any user attempted login the application would get a 403 Error relating to CSRF issue as soon as the user clicked the Login button.</p>
<p>I initially thought this was a Microsoft Edge issue. Without being prefaced with https://, Edge defaulted to http:// connection. If I entered the entered the site as https:// there would be no login issues. Possibly a security issue or setting on the Edge browser?, not a browser that I use.</p>
<p>Having checked further I found that if I used http:// on Google Chrome I was able to replicate the 403 error and so the issue was not unique to Microsoft Edge.</p>

<span style="color:#ebd80c; font-weight:bold; font-size:14px">Initial Fix.</span>

<p>I checked code and found all csrf_token's were located correctly in the relevant forms and I could see not issues in the views.py. My initial fix to the issue was to create a custom 403 page.</p>
<p>When triggered by a 403 Error the custom 403 page would revert the user back to a secure HTTPS connection, https://an-seo.herokuapp.com, and the application would be fully functional from that point.</p>

<span style="color:#ebd80c; font-weight:bold; font-size:14px">Further Investigation Of Issue.</span>

- Investigation of similiar issues suggested adding CSRF specific settings the settings.py But of these related to Django 4+ and not Django 3 as I am using. Having experimented with these settings I found that they had no impact on the issue.    

