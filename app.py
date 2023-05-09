from flask import Flask, jsonify, abort, request, url_for
from models import Event, OnlineEvent, events


app = Flask(__name__)


@app.route("/api/events/")
def list_events():
    """List all events"""
    events_dict = [event.__dict__ for event in events]
    return jsonify(events_dict)


@app.route("/api/events/<int:id>/")
def event_details(id):
    """Return an event"""
    event = get_event(id)
    return jsonify(event.__dict__)


@app.route("/api/events/", methods=["POST"])
def add_event():
    """Add a new event"""
    json_data = request.get_json()
    name = json_data.get("name", None)
    address = json_data.get("address", None)
    if not name:
        abort(400, "'name' must be specified")

    if address:
        new_event = Event(name=name, address=address)
    else:
        new_event = OnlineEvent(name=name)

    events.append(new_event)
    return {
        "url": url_for("event_details", id=new_event.id),
        "id": new_event.id,
        "name": new_event.name,
        "address": new_event.address,
    }


@app.route("/api/events/<int:id>/", methods=["DELETE"])
def delete_event(id):
    """Delete an event"""
    event = get_event(id)
    events.remove(event)
    return (jsonify(id=event.id), 200)


@app.route("/api/events/<int:id>/", methods=["PUT"])
def edit_event(id):
    """Edit event"""
    json_data = request.get_json()
    name = json_data.get("name", None)
    address = json_data.get("address", None)

    if not name:
        abort(400, '"name" is required')
    if not address:
        abort(400, '"address" is required')

    event = get_event(id)
    event.name = name
    event.address = address

    return event.__dict__


@app.route("/api/events/<int:id>/", methods=["PATCH"])
def edit_partial_event(id):
    """Edit partial event"""
    json_data = request.get_json()
    event = get_event(id)
    if "name" in json_data.keys():
        name = json_data.get("name")
        if not name:
            abort(404, '"name" is required')
        event.name = name
    if "address" in json_data.keys():
        address = json_data.get("address")
        if not address:
            abort(404, '"address" is required')
        event.address = address

    return event.__dict__


@app.errorhandler(400)
@app.errorhandler(404)
def handle_status(erro):
    """Handle erros status code"""
    return (jsonify(erro=erro.description), erro.code)


def get_event(id):
    """Select an event"""
    for event in events:
        if event.id == id:
            return event
    abort(404, "Event not found")
