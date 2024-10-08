Directory structure
===========================
Following is the structure of the code base

.. code-block::

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


`config` directory contains logging and other settings of the project and is utilised by all the 4 entrypoints of the package.
`load`, `categorize`, `dashboard`, `docs`

These options are:

.. code-block::

   python -m vanilla_steel load --source 1
   python -m vanilla_steel load --source 2
   python -m vanilla_steel load --source 3
   python -m vanilla_steel categorize
   python -m vanilla_steel dashboard
   python -m vanilla_steel docs --serve

