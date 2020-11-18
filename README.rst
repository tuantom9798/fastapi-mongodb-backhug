
What for
----------
This project is a realworld backend based on fastapi+mongodb. It can be used as a sample backend or a sample fastapi project with mongodb.


Quickstart
----------
Setup development environment

Install miniconda

    conda env create -f environment.yml

Activate py3_pacla_api_endpoint_fastapi environment:

    source activate py3_pacla_api_endpoint_fastapi

  DO NOT use the same conda environment for 2 different projects.


Install requirement

Make sure that the conda environment py3_pacla_api_endpoint_fastapi has been activated by checking the output of the command
conda info --envs

    pip install -r req.txt

To run the web application in debug use::

    uvicorn app.main:app --reload


Deployment with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create ``.env`` file like in `Quickstart` section or modify ``.env.example``. ``MONGO_HOST`` must be specified as `db` or modified in ``docker-compose.yml`` also. Then just run::

    docker-compose up -d

Application will be available on ``localhost`` or ``127.0.0.1`` in your browser.

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` directory. ``alembic`` is directory with sql migrations.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   └── routes       - define web routes.
    ├── core             - application configuration, startup events, logging.(jwt, security, configuration)
    |   |__errors        - definition of error handlers.
    |   |__config        - MongoDB, Host, Port, Project Name,..
    |   |__jwt           - functions use jwt to decode or encode (token, current_user)
    |   |__utils/security- general functions, hash/verify password
    | 
    ├── db               - db related stuff.
    │   ├── mongo_utils  - general functions support for mongodb (open/close connection) 
    │   └── mongodb      - Initialization database
    |   |__ migration    - create collections to migrate and dummy data
    ├── models           - pydantic models for this application.
    ├── util             - All utils in b
    ├── crud             - logic and crud of all collections
    └── main.py          - FastAPI application creation, configuration and api router including.

Todo
----
1) Add more unit test
