# Fullstack Challenge

Welcome to our fullstack challenge! :wave:

## Setup

1. Please upload this repository to your git
2. You will need to have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed
3. Install the frontend
   ```shell
   $ cd frontend
   $ yarn install
   ```
4. To start the Frontend + API + DB run:
   ```shell
   $ docker-compose up
   ```
5. If you install a new package for the frontend, you will need to stop the docker-compose and rebuild the frontend:
   ```shell
   $ docker compose build frontend
   ```

The frontend runs on `localhost:3000`

The API runs on `localhost:20002`

- if you fetch client side in the frontend use `localhost:20002` as the base url, if you fetch server side in the frontend use `api:20002` as the base url
- in `fullstack_challenge_api/routes/companies.py` there is a example on how to use the DB in an endpoint.
  You need to write `db: Session = Depends(get_db))` as a parameter, then you can use the `SQLAlchemy` session. The setup is already done.

The DB runs on `localhost:3306`.

- You should find the necessary information in the `api/config` directory.

## Challenge

You will need to create a full deployment of a NextJS frontend + FastAPI API + MySQL DB.
The setup for the frontend, API and DB is already done, so you only need to add you code.

You'll find a `challenge_companies.json` and `challenge_deals.json` in the `data`-folder of this repository.

1. Import the Data from the `JSON files` to the `MySQL DB`
2. Create a `GET` endpoint in the `FastAPI` for both `companies` and `deals`
3. Display the `companies` and their `deals` with their information in the `NextJS` frontend

- `companies` have a 1 to N relationship with `deals`
  - e.g. 1 `company` can have N `deals`
  - every 1 `deal` is part of 1 `company`
