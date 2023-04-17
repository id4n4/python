from flask import Flask, jsonify, request
from products import products


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message" : "hello work!!"})

@app.route("/products")
def getProducts():
    return jsonify({
        "products": [products],
        "message": "Products OK"
        })

@app.route("/products/<string:product_name>")
def getProduct(product_name):
    # crea una nueva lista que contiene solo los elementos de la lista 
    # products cuyo valor en la clave 'name' coincide con el valor de la 
    # variable product_name. Es una forma concisa y legible de filtrar una 
    # lista de diccionarios en Python.
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0) :
        return jsonify({
            "product": productsFound[0]
        })
    else:
        return jsonify({
            "message": "Product not found"
        })
    

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    print(request.json)
    return jsonify({
        "message": "Product added Succesfully",
        "products": products
    })

@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "products": products
        })
    return jsonify({
        "message" : "Product not found"
    })

@app.route('/products/<string:product_name>',methods=["DELETE"])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({
        "message": "Product not found"
    })

if __name__ == "__main__":
    app.run(debug=True, port=4000)