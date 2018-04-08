Python Socket Calculator

how to use:
- run "python server.py" in terminal
- run "python client.py" in another terminal
- insert the ip of the server, or "127.0.0.1" if run locally
- insert operator
- insert first operand
- insert second operand
- server will send the result of the computation then client will print the result
- type "exit" to exit the program, just press enter to continue

server.py explanation
- 1st line to import the library
- 3rd line to create socket object
- 4th line to bind the program to port 3000
- 6th line to restrict server to only listen to 1 client
- 7th line to accept incomming connection
- 10th line to prepare the variable
- 11th - 18th line to recieve data from client and then append it into list
- in line 12th if the first data to be recieved is "exit" then the program will exit
- 19th - 26th line to calculate the data
- 28th line to send the data to the client

client.py explanation
- 1st line to import the library
- 3rd line to create socket object
- 5th line to connect to the server
- 8th - 10th line to input the operator, operandA, and operandB
- 11th - 13th line to send the data to server
- 14th line to recieve the result and then print it to the console
- 15th line to ask the user wether the user want to exit or continue
- 16th - 18th line to exit the program if the user want to exit