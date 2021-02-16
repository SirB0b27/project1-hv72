# Spotify Artists Top Track Preview Application 
### by Hemanth Velan

# Install Requirements:
1. `pip install python-dotenv`
2. `pip install requests`
3. `npm install -g flask`
4. `npm install -g heroku`


#Spotify API Setup
1. Head to `https://developer.spotify.com/dashboard/login`
2. Login with your spotify account, if not create one
3. Click to create an app
4. Give it a name and a discription
5. You should see your Client ID
6. Click to reveal Client Secret
7. Have Client ID and Secret at the ready

# Setup
1. Create `.env` file in your project directory
2. Add your client ID + secrets for Spotify and token for Genius in this format to `.env`:

    `export Client_ID="{YOUR CLIENT ID}"`
    
    `export Client_Secret="{YOUR CLIENT SECRET}"`
    

#Deploying on Heroku
1. Go to `https://www.heroku.com/` and create an account to deploy to Heroku
2. Create a requirements file by running: `touch requirements.txt`
3. Run `pip freeze > requirements.txt`
4. Create a Procfile by running: `touch Procfile`
5. open `Procfile` and add the line: `web: python app.py`
6. Commit and push to github by running: `git commit -m "message of your own"` followed by `git push origin main`
7. Login to Heroku by running `heroku login -i`
8. Enter your login credentials for Heroku
9. Run `heroku create` to create an application on Heroku
10. Push to heroku by running `git push heroku main`
11. Run the command `heroku open` to open the heroku site.
    If it doesnt open, it will give you a manual link to open in your browser with


#Genius API Setup
1. Head to `https://docs.genius.com/`
2. Click on `API client management page`
3. Login or Signup for an account
4. Click on `New API Client`
5. Give it a name
6. Enter the URL from Heroku for `App Website URL`
7. Click on `Generate Access Token` to get the access token for Genius API
8. Add your Genius Access Token to `.env` in the following format:
    
    `export Genius_Token="{YOUR GENIUS TOKEN}"`


# Push Genius API Changes to Github and Heroku and view the site
1. Run `git commit -m "message of your own"` followed by `git push origin main`
2. Run `git push heroku main` to push to heroku
2. Run `heroku open` to run the application and view the site
3. If it doesnt open, there should be a link to visit manually, 
    click on link to view the site


# Additional Features to Implement in the Future
1. Allowing the user to search for their own artists.
    I plan on using this api to get the artist ID:
    `'https://api.spotify.com/v1/search?q=Artist+Name&type=artist'`
2. Bluring the background color of the preview div.
    I plan on doing this by adding a `filter: bulr(#px)`, but an issue with this is that this adds a blur to all sub tags, 
    so will need to figure out how to unblur the sub tags


# Technical Issues
1. Fix 404 issues with song preview link:
    1. Noticed that my application was returning 404 in the terminal
    2. So I look a look at what aspect of the website was causing the issue
    3. Narrowed down to preview audio, as it wasn't pointing to the correct link
    4. Recalled reading in Slack about someone having issues with song preview links
    5. Printed out what the output for song preview link, found out the song with issues printed None
    6. Tried to do an if statement in jinja comparing the variable to "None"
    7. This didn't work, because the None being printed out was of type None, not string None(found out by looking up None issue on StackOverflow)
        StackOverflow Link: `https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object/34570099`
    8. I proceeded to do an if statement in python to check if its of None type, if so set it to string None
    9. Proceeded with doing string comparison in jinja, where it worked correctly

2. Padding issue between by song preview and top track list
    1. After separating the preview and top track list into their own divs, noticed there was some blank space between the divs
    2. Went straight to google to figure out how to remove the whitespace
    3. Noticed that the solution was related to padding and margin
        StackOverflow Link: `https://stackoverflow.com/questions/18315507/remove-margin-between-divs`
    4. Recalled from my IT202 class that you can specify which side of the div you want to modify
    5. So I did the padding and margin modification to the bottom of the song preview div and the top for the track list div

3. Had issues with figuring out how to set up header and parameter for Genius API
    1. Was trying to get the Genius API working, but hit wasn't working correctly
    2. Realized that if I had just scrolled down on the documentation, the answer was right there
    3. Scrolled down to `Authentication` category
    4. Read the documentation and modified my code to work