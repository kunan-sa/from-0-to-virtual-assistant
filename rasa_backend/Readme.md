# __Rasa: installation and execution__

## __Setting up the Virtual Environment__
Why set up a virtual environment? Virtual environments let you scope Python packages to a project directory, instead of installing the package on the system (global) level. This means you can use different versions of a package for different projects and helps to prevent conflicts.

We’re using **venv** in this demo to create the virtual environment, because it’s built into the Python standard library. This process is recommended for Mac and Linux users.

> **Note for Windows Users**: If you’re using Windows, we recommend using Anaconda to set up your virtual environment instead of **venv**. We have detailed instructions <a href="/windows_installation.md">here</a> and this [video tutorial](https://www.youtube.com/watch?v=4ewIABo0OkU) to help. The important parts to note are installing ujson, tensorflow, and the Visual Studio C++ build tools.

For the tutorial, we’ll be working with an existing Rasa project instead of creating a new one using ```rasa init``` (the recommended method when building your own bot from scratch), so be sure to clone this project using ```git clone https://git.democrm.com.ar/ia/from-0-to-virtual-assitant.git``` and install the dependencies (instructions below).

#### __Steps (Mac/Linux):__

* Inside the root directory of this project
* Create the virtual environment
    * ```python3 -m venv ./venv```
* Activate the virtual environment
    * ```source ./venv/bin/activate```

> NB: In order to leave the virtual environment simply use the command
>    ```deactivate```

> to delete/ remove with
> ```rm -rf venv```

#### __Install dependencies__

To install [Rasa Open Source](https://rasa.com/docs/rasa/) (along with the other packages required by the PyData Conference Assistant), we’ll use the requirements.txt included in the repository.

* Make sure you are in the root directory of this project
* Upgrade pip
    * ```pip install --upgrade pip```
* Install dependencies
    * ```pip install -r requirements.txt```

## __Rasa__ <a name="rasa"></a>

For the Rasa assistant to work, first we need to download and assign a language model to it.

#### __Download the SpaCy Language Model__
[SpaCy](https://spacy.io/usage/models) is a Python package used for advanced Natural Language Processing. We will use their English language model for help with intent classification.

* Download the model:
    * ```python3 -m spacy download en_core_web_md```
* Link the model:
    * ```python3 -m spacy link en_core_web_md en```

#### __Train and Run the Assistant to use it on shell__
Before we can start talking to the assistant, we need to train the model and start the servers.
* Change to the rasa_backend directory

    ```cd rasa_backend```

* Train the model

    ```rasa train```

* Once the model has finished training, start the Rasa Open Source server. This will also start a session to chat with the assistant on the command line.

    ```rasa shell```

> Talk to the bot!
> To stop the Rasa Open Source server and the chat session, type /stop

#### __To run the assistant and use it with a frontend__
If you want to connect rasa bot with the frontend, you need install and run the frontend (see [Frontend](#frontend)) and run rasa with this command:

```rasa run --enable-api --cors "*" --debug```

> By default rasa runs on port 5005

> You can specify a port with the flag `-p` 

> for example ```rasa run --enable-api --cors "*" --debug -p 5006```

<br>
<br>
<br>
<a href="../README.md">Back to main readme</a>