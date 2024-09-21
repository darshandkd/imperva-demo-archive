from flask import Flask, jsonify, request

app = Flask(__name__)

DUMMY_API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc" # Example of a dummy secret

# Sample data store
data_store = {
    1: {"name": "Item 1", "description": "This is item 1"},
    2: {"name": "Item 2", "description": "This is item 2"}
}

@app.route('/api', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from the API!"})

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data_store)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_id = max(data_store.keys()) + 1
    data_store[new_id] = new_item
    return jsonify({"id": new_id, "item": new_item}), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    if item_id in data_store:
        data_store[item_id] = updated_item
        return jsonify({"id": item_id, "item": updated_item})
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        del data_store[item_id]
        return jsonify({"message": "Item deleted"})
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

