****************************
Google calendar test framework
****************************

Getting Started
===================
These instructions will help you to get a copy of the project and run it on your local machine for development and
executing test scripts.

Python version
==============
Python version 3.7 is required.

Installing
==========

1. Clone repository from github

.. code-block:: bash

    git clone git@github.com:AnastasiiaLatysh/google_service_api.git

2. Execute next commands in terminal

Create a virtual environment (Optional)

.. code-block:: bash

    virtualenv --python=python3.7 .venv
    source .venv/bin/active

Install requirements

.. code-block:: bash

    pip install -r requirements.txt

3. Add .env file and fill it with appropriate data according to .env.example.

4. Run tests

.. code-block:: bash

    pytest tests/
