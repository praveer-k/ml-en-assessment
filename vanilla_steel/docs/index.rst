Welcome to Vanilla Steel docs!
=================================

Supplier Data Standardization for Metal Trading
-----------------------------------------------

Hopefully you reached this documentation using the following the command:

.. code-block:: bash
   
   cd vanilla_steel
   poetry shell
   poetry install
   poetry run docs --serve

Quick overview:

.. toctree::
   :maxdepth: 3

   pages/problem_statement
   pages/directory_structure
   pages/architecture

The project has a few dependencies:

- |postgres_image|  |postgres_local_link|
   Postgres is the database used in this project to display data on the dashboard.

- |streamlit_image|  |streamlit_local_link|
   streamlit allows us to quickly create dashboard using its apis. Run it manually to see the dashboard using `python -m vanilla_steel --dashboard`.

- |ollama_image| 
   Ollama is the large language model environment used to run llms locally

These dependencies are installed in an isolated environment using docker compose. 

You can run the docker compose up command to start the dependent instances of postgres and ollama.

.. code-block:: bash
      
   docker compose up -d

Postgres instance creates a database called `vanilla_steel`.

This allows us to have a pre-configured environment to run load and categorize commands. Now we can load and categorize data and, eventually, visualize it on a dashboard.

We now need can build the python module that can be used from anywhere.
To build it run the following command:

.. code-block:: bash
      
   poetry build

You can now run the following commands in sequence to load, categorize and show data.

.. code-block:: bash

   python -m vanilla_steel --load --source 1
   python -m vanilla_steel --load --source 2
   python -m vanilla_steel --load --source 3
   python -m vanilla_steel --categorize
   python -m vanilla_steel --dashboard

That's it !

.. |postgres_image| image:: _static/postgres.svg 
   :height: 1.2em
   :width: 1.2em

.. |ollama_image| image:: _static/ollama.svg
   :height: 1.2em
   :width: 1.2em

.. |streamlit_image| image:: _static/streamlit.svg
   :height: 1.2em
   :width: 1.2em

.. |postgres_local_link| raw:: html

   <a href="http://localhost:5000" target="_blank">Postgres Instance</a>

.. |streamlit_local_link| raw:: html
   
   <a href="http://localhost:8501/docs" target="_blank">Streamlit Instance</a>


