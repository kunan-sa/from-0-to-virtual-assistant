
# Prerequisites

* [Install latest node and npm](https://nodejs.org/es/download/)
> [Recommended but not needed]. Install a npm version manager. I use [this python one, nodeenv](https://pypi.org/project/nodeenv/)

# Installation

```bash
//git clone this repo
git clone githublink

//enter the frontend directory
cd frontend

//install the project
npm install
```
#Usage
## Run locally
```bash
npm run dev
```

## Compiling the code
```bash
npm run build
```

## Hand-off variables

In `src/constants.js` there are **handoff variables**:
* `BOT_URL`       //bot endpoint

* `HUMAN_URL`     //human endpoint

* `TO_HUMAN_TRANSFER_TEXT` //line your bot must say
                           //so the front makes the transfer to human
                           //for ex.: "You are being transferred to a human!"

* `TO_BOT_TRANSFER_TEXT` //line the human must say
                         //so the front makes the transfer to bot
                         //for ex: "End"

