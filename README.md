# atypica-backend
The backend of the Atypica App, an AI educational tool for accessibility for the neurodivergent community.

## Installation
Install Ollama in your local machine; consult the [detailed instructions for installing ollama here](https://ollama.com/download/). For Linux environments, use the following command.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

After this, install the requirements on your python environment. We suggest the creation of an isolated python environment for this, that can be created as follows.

```bash
python3 -m venv env
```

In this case, activate the environment.

```bash
source env/bin/activate
```

Finally, install all the python requirements.

```bash
pip install -r requirements.txt
```