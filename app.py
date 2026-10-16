from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message= "Hello from azure contianer App!")

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)


# def get_message():
#     return "Hello from DevOps!"

# def login(username):
#     if not username:
#         raise ValueError("Username is required")
#     return f"Welcome, {username}!"


# def login(username):
#     if not username:
#         raise ValueError("Username is required")

#     return f"Welcome, {username}!"


# if __name__ == "__main__":
#     print(get_message())
