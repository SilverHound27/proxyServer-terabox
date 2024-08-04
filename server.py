import time
from quart import Quart, Blueprint, render_template, request, jsonify, abort
import uvicorn
import asyncio
from extractor_tera import make_connection
from crypto import encode_string,decode_string
from os import environ as env
from sample import mock_data


SERVER_URL = env.get("SERVER_URL", "http://127.0.0.1:8080")
BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
PORT = int(env.get("PORT", 8080))

app = Quart(__name__)

# List of allowed IP addresses
ALLOWED_IPS = {'13.228.225.19', '18.142.128.26', '54.254.162.138'}

# Middleware to check IP address
@app.before_request
async def restrict_ip():
    if request.path == '/proxyapi':
        client_ip = request.remote_addr
        print(client_ip)
        if client_ip not in ALLOWED_IPS:
            print("IP Unlisted")
            abort(403)  # Forbidden


@app.route('/proxyapi')
async def dlapi():
    query = request.args.get('data')

    if query:
        try:
            url = decode_string(query)
            with open("log.txt", "a") as f:
                f.write(f"{time.ctime()} | {query}\n")
                
        except Exception as e:
            return jsonify({"error": "Invalid file ID."}), 400
    else:
        return {"error": "No query Found"} , 400

    if not url or 'tera' not in url.lower():
        return jsonify({"error": "Use a valid Terabox URL."}), 400

    
    data_json, status = make_connection(url)
    # data_json, status = y, 400 # TESTS

    if status != 200:
        return jsonify({"error": "Some error occurred, try again later.", "data": data_json, 'code': status}), 400
    
    data = encode_string(str(data_json))
    return data

@app.route('/health')
async def proxytest():
    return "Good", 200


@app.route('/mock')
async def mock():
    return encode_string(str(mock_data))

# @app.route('/<path:path>')
# async def catch_all(path):
#     return "SUCESS", 200

@app.errorhandler(404)
async def handle_404(error):
    return '', 404  # Send an empty response with a 404 status code


uvicorn.run(app, host=BIND_ADDRESS, port=PORT)