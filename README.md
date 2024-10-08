# Vanilla Steel

## Supplier Data Standardization for Metal Trading

### Requirements

In order to run the application you need to have java, graphviz, docker, python 3.12 and poetry installed on your machine

You can use the following link to install the dependencies:

- https://www.oracle.com/java/technologies/downloads/
- https://graphviz.org/download/
- https://docs.docker.com/engine/install/
- https://www.python.org/downloads/
- https://python-poetry.org/docs/

Once the above dependencies are installed clone the repository and cd into the directory

Within the repository directory, run the following command:

```bash
docker compose up -d
poetry shell
poetry install
python -m vanilla_steel docs --serve
python -m vanilla_steel dashboard
python -m vanilla_steel load --source 1
python -m vanilla_steel load --source 2
python -m vanilla_steel load --source 3
python -m vanilla_steel categorize
```

Following is the directory structure of the project:

```text
ml-en-assessment
├── notebooks
├── resources
├── task_scripts
├── vanilla_steel
│   ├── config
│   ├── dashboard
│   ├── database
│   ├── docs
│   ├── modeling
│   ├── task_organizer
│   └── __main__.py
├── .env
├── ...
├── docker-compose.yaml
├── Dockerfile
├── pyproject.toml
├── README.md
└── specifications.yaml
```

Rest of the details can be found in the docs.

In future we would use data drift measure to check the quality of the data.
