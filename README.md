# From 0 to virtual assitant

This project accompanies the PyData 2020 Global tutorial "[From 0 to Virtual Assistant (Now with human handoff!)](https://global.pydata.org/talks/from-0-to-virtual-assistant-now-with-human-handoff)".

This repository has everything you need to build a chatbot with human handoff. You will need to install the required packages and run each of the three elements on your local computer. We recommend that you do the installation and execution in this order (click links below for instructions):
* <a href="/rasa_backend/Readme.md">1° Rasa</a>
* <a href="/router_backend/Readme.md">2° Router</a>
* <a href="/frontend/Readme.md">3° Frontend</a>

You will find a _Readme.md_ file in each folder.

Once this is finished, you will have to [run the three parts together](#conn) on three seperate servers.

<img src="/images/arq.png" width="600"/>

## Prerequisites to backend

Before you begin, you’ll need:
* IDE or Text editor
* Python 3.6 or 3.7

## How to connect the three parts <a name="conn"></a>

You'll need to have three tabs on your terminal or three terminals open, in each running each of these parts.

> That is, one server for the bot, one for the router and one for the frontend.

In the file `frontend/src/constants.js` the urls should be specified with the Rasa endpoint and the router endpoint.

If everything has been configured correctly, the frontend the input should be enabled successfully and you should be able to talk to your bot!

Upon requesting for a human transfer, the bot should answer with the `TO_HUMAN_TRANSFER_TEXT` line and the handoff should happen, updating the front to inform you of the successful transfer!

## Troubleshooting
> If the input of the chat is disabled and there appears a server connection error check:
> * Have the URLs been correctly set? (check for any http vs https typos)
> * Am I running the Rasa chatbot correctly? (should be run **with cors enabled**)
