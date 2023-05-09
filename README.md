# Flask CRUD API to Events

This project is a simple Flask API that performs CRUD operations on events with name and location information.

## Quick Start

### Clone this repository

```bash
git clone https://github.com/diogosaucedo/first-steps-flask.git
```

### Access the directory

```bash
cd first-steps-flask
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run server

```bash
flask run
```

### Access `http://localhost:5000/api/events`

## Endpoints

### GET /api/events

Returns a list of events

### GET /api/events/{int:id}

Return an event

### POST /api/events

Create a new event

Exemple:

```json
{
    "name": "My Event",
    "address": "My city"
}
```

### PUT /api/events/{int:id}

Update a event fully

Exemple:

```json
{
    "name": "Event Name",
    "address": "New City"
}
```

### PATCH /api/events/{int:id}

Event partial update

Exemplo:

```json
{
    "name": "Feira do pastel",
}
```

### DELETE /api/events/{int:id}

Remove an event.
