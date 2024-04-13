# Web API Template

A template repository for creating a web API using Django and Django REST framework.

## Local development

At project root, perform the following.

1. Use python 3.12
    ```console
    $ pyenv install 3.12
    $ pyenv local 3.12
    ```
2. Install poetry
    ```console
    $ brew install poetry
    ```
3. Set up virtual environment
    ```console
    $ poetry env use 3.12
    $ poetry install
    ```
4. Apply migrations and create a superuser for testing purposes (use `password` for password)
    ```console
    $ make migrate
    $ poetry run python manage.py createsuperuser --username admin --email admin@example.com
    ```
5. Create a personal config file (replace `<API_KEY>` and `<URL>` with the appropriate values, this is to avoid having sensitive information in the codebase)
   ```console
   $ touch web_api/config/local.py
       or
   $ make local
   ```
6. Run the server
    ```console
    $ ENVIRONMENT=local make serve
    ```
