# From 0 to virtual assistant
## Installing Rasa for Windows 

- First, install Anaconda: https://www.anaconda.com/products/individual/get-started

- While installing Anaconda, at the Advanced Installation Options, click "Add Anaconda to my PATH environment variable" (yep, the not recommended option).

- When the installation of Anaconda is over, launch the Anaconda shell: Click on  "Search", type "Anaconda Prompt" and click on it.

- Go into the directory where you want to build the bot: e.g.:
 cd C:\Users\<your name?>\Documents\rasa_backend

- Create a new Conda environment, this will allow to have all the dependencies together in a single centralized place: 

```conda create --name rasa_env python==3.7.6 ```

Specify the version of Python that you have installed in your Conda distribution. Confirm the process.

- Activate the environment: 

```conda activate rasa_env```

You will note that the env has changed from the "base" env to "installingrasa" env.

- Other things you have to do...enter the following commands in the same shell where the environmet "installingrasa" is running: 

```
conda install ujson 
conda install tensorflow
```

- Once that is finished, install Rasa via pip:
```
pip install rasa
```

- In order to run Tensorflow on Windows you have to download Visual Studio C++ separately: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

- Come back to the "installingrasa conda environment", and try initializing a new bot. Enter:

```
rasa init
```

- The shell will respond you: Do you want to train an initial model? Type "yes".

- After the bot has finished training, the prompt will ask you: Do you want to speak to the trained assistant on the command line?


## Why do we have to install Rasa with conda?

It's generally easier to use conda than pip for TensorFlow, specifically because conda handles the CUDA dependencies while pip does not. Conda installs of Tensorflow have also been shown to be more performant. 

