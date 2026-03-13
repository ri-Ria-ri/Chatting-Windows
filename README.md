## 📃 Overview: 

  Language: Python 

    • A real time text based chat between server and user 

    • Server-Client archictechture using Python sockets 

    • Simple, lightweight design for learning 

    • It uses HMAC (Hash-based Message Authentication Code) with SHA-256 to ensure message integrity between client and server. 

    • Each message is verified against a shared secret key before being accepted.

## 🧰 Tools: 

  • Python 3.14.0  

    Libraries:
     • socket
     • hmac
     • hashlib 

  • Windows OS (Tested on Windows 11) 
   
## ⚙️ Features: 

  • Server listens for incoming TCP connections 

  • Messages are verified using HMAC_SHA265 
   
  • Prevents tampering by rejecting altered messages 

  • Supports interactive replies from the server 

  • Chat is exited when the client types "exit" 
  

## 🖼️ Structure: 
  
     secure-chat
         │
         ├── server.py
         ├── client.py
         |__ README.md  

## 👟 How to Run: 
   Ⅰ. Run the Server by typing the below command on the   terminal: 

      python server.py  
    
    The server will start listening on 0.0.0.0:12345
  Ⅱ. Connect to the client by splitting the terminal and running the following command: 
   
     python client.py 
    
    When the client connects; the server and the client can chat


  Ⅲ. To exit:
     Type "exit" from the client to close the connection