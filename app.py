from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

@app.route('/', methods = ['GET'])

# Definir la ruta antes iniciar el servidor
def diHola():
    name = request.args.get('name')
    
    if name is None:
        txt = "Hello !"
    else:
        txt = f"Hello {name} !"

    return jsonify({"message": txt})

# Incia el servidor
if __name__  == '__main__':
    app.run(debug=True, port=8000)
