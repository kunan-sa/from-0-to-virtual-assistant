# __4. Frontend__

#### __Prerequisites__

* [Install latest node and npm](https://nodejs.org/es/download/)
> [Recommended but not needed]. Install a npm version manager. I use [this python one, nodeenv](https://pypi.org/project/nodeenv/)

#### __Installation__

```bash
//enter the frontend directory
cd frontend

//install the project
npm install
```

#### __Usage__

__Run locally__

```bash
npm run dev
```
> By default the process runs on port 8080

> A browser tab should be open with the frontend running, but in case that doesn't happen
> > Open a browser and go to
> > `http://localhost:8080`

__Compiling the code__

```bash
npm run build
```

__Hand-off variables__

In `frontend/src/constants.js` there are **handoff variables**:

* `BOT_URL`       //bot endpoint

* `HUMAN_URL`     //human endpoint

* `TO_HUMAN_TRANSFER_TEXT` //line your bot must say
                           //so the front makes the transfer to human
                           //for ex.: "You are being transferred to a human!"

* `TO_BOT_TRANSFER_TEXT` //line the human must say
                         //so the front makes the transfer to bot
                         //for ex: "End"

<br>
<br>
<br>
<a href="../README.md">Back to main readme</a>