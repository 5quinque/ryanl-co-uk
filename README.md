# ryanl-co-uk

## Docker

```bash
docker build --tag ryanl .
docker run --name web-ryanl \
    -e DATABASE_HOST=db_host \
    -e DATABASE_NAME=db_name \
    -e DATABASE_USER=db_user \
    -e DATABASE_PASS=db_password \
    -e VIRTUAL_HOST=ryanl.co.uk,www.ryanl.co.uk \
    -e LETSENCRYPT_HOST=ryanl.co.uk,www.ryanl.co.uk \
    --net web \
    -d ryanl
```

## Dev

### Install dependencies

```bash
pipenv install --ignore-pipfile
```

To activate the virtual environment

```bash
pipenv shell
```

### Setup pre-commit hook 

```bash
pre-commit install
```

Update linter and formatting tools by running this command

```bash
pre-commit autoupdate
```