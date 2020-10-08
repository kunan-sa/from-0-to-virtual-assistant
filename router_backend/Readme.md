# Router

In this section we will do the following:
* __Install ngrok__: this is to expose the endpoint of the router that runs locally.
* __Run the router__: this is the server that manages the interaction between front and slack when human handoff is active.
* __Create slack app__: this is needed to interact with slack api.

Below you have all steps to do this, but just in case we recorded a video with the tutorial for this part. [See here](https://youtu.be/iHfFmwS-fsc)

Go for it!


#### __Install ngrok__

Follow the instructions here to download and install ngrok: https://ngrok.com/download

>**Note: If you’re on a Mac**, the easiest way to install ngrok is using homebrew. This method installs globally, so you can run the ngrok command from any directory.
>```
>brew cask install ngrok
>```

If you installed ngrok by downloading the file directly (not using homebrew), you’ll need to provide the path to where you unzipped the ngrok executable (relative to your project folder) when you start ngrok (e.g. `./ngrok http <port>`). Alternatively, you can add the ngrok executable to your `$PATH` so you can run the ngrok command globally.

#### __Run the router__

* In new terminal activate the virtual environment
``` source ./venv/bin/activate ```

> **Note for Windows Users**: If you have installed the backend packages (Rasa) using anaconda (as we recommend) then you should activate your environment using conda":
```conda activate rasa_env```

* Move to router directory
``` cd router_backend ```

* Run the router
``` python main.py ```

By default this run on port 8000. If you want to change this, on main.py, to the end, you can especify another port in line: app.run(host="localhost", port=8000)

* With ngrok exposed, run the server:
``` ngrok http 8000 ```

Here, you are going to see an url on your terminal. Next you will need to replace `http://<yyyyyy>.ngrok.io/webhook` with this.

<img src="/images/ngrokrunning.png" width="500"/>


#### __Create Slack App__

1. On https://api.slack.com/apps -> Create new app
<br> - Set App name
<br> - Choose Slack workspace
<br> - Create App

2. On tab OAuth & Permissions
<br> - Set to "Redirect URLs" -> Add New Redirect URL -> http://<yyyyyy>.ngrok.io/webhook -> Add -> Save URLs

3. On tab Event subscriptions
<br> - Set Enable events to -> on
<br> - Set the Request URL -> http://<yyyyyy>.ngrok.io/webhook
<br> - Subscribe to bot events -> Add Bot User Event -> choose message.channels (to talk on a public channel)
<br> - Save changes

4. (Optional) App Home -> Always Show My Bot as Online -> on

5. Again on tab OAuth & Permissions
<br> - On section Scopes, add to Bot Token Scopes the following:
<br> __ channels:history
<br> __ channels:manage
<br> __ channels:read
<br> __ chat:write
<br> __ im:write
<br> __ users:read
<br> - Then on the top -> Install app to workspace -> Allow
<br> It generates:
Bot User OAuth Access Token: xoxb-<wwwwwwwwwww>-<yyyyyyyyyyy>-<xxxxxxxxxxxxxxxxxxx>

6. Add the following lines to `router_backend/constants.py`:
* `SLACK_APP_TOKEN` = `<Bot-User-OAuth-Access-Token>`
* `OPERATOR_NAME` = `<your-name-in-slack>`

    > This is the first part or local address of the email used to register in Slack, i.e.: john.roberts@gmail.com -> 'john.roberts'

After that, you need restart the router to take changes.

That is all in this section!!


#### __If at any point you run ngrok again and you just need to change the webhook url:__
In case, in the future, you want to change the webhook url of your slack app:

* Register the ngrok webhook address in in the Slack App
    - webhook: `https://<yyyyyy>.ngrok.io/webhook`
    - Add this url to your Slack App:
        - In _OAuth & Permissions_ -> _Redirect URLs_ -> add url -> _SaveURLs_
        - In _Event Subscriptions_ -> _Enable Events_ -> change _request url_ -> _Save changes_ (at this point the router backend needs to be running because Slack makes a "challenge" of the url in order to enable that url)
    - Return to _OAuth & Permissions_ -> Reinstall App


<br>
<br>
<br>
<a href="../README.md">Back to main readme</a>
