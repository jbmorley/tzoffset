# tzoffset

Lightweight service to give the UTC offset for a given timezone

## Development

Install the dependencies:

```bash
pipenv install
```

Run a local instance for development:

```bash
pipenv run heroku local
```

Manually test the functionality using `curl`:

```bash
curl http://0.0.0.0:5000/api/v1/offset/
```

## Production

See https://tzoffset.io.

```bash
curl https://tzoffset.io/api/v1/offset/Europe/Paris
```
