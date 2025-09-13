from flask import Flask, request, jsonify

app = Flask(__name__)
inventory = {}

# List all items
@app.route('/items')
def list_items():
    return jsonify(list(inventory.values()))

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    inventory[data['id']] = data
    return jsonify(data)

# Get item by id
@app.route('/items/<item_id>')
def get_item(item_id):
    item = inventory.get(item_id)
    return jsonify(item) if item else ('Item not found', 404)

# Update item by id
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    inventory[item_id] = {**inventory.get(item_id, {}), **data}
    return jsonify(inventory[item_id])

# Delete item by id
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    removed = inventory.pop(item_id, None)
    return jsonify(removed) if removed else ('Item not found', 404)

if __name__ == "__main__":
    app.run()
