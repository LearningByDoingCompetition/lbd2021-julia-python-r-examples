from random import random
import zmq

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("ipc://socket")

    print('This is the Python controller')

    while True:
        query = socket.recv_json()
        # query["system"]    – robot name
        # query["init"]      – new robot/trajectory? true/false
        # query["d_control"] – length of required input control
        # query["state"]     – system state variables
        #                      (same order as the columns in the training data,
        #                       X, Y, Xi, Yi, ..., dX, dY, dXi, dYi, ...)
        # query["position"]  – x,y coordinates current position
        #                      (same as first two elements of query["state"])
        # query["target"]    – x,y coordinates of next target position

        if query['init']:
            print(f"Initialising controller for {query['system']} "
                  "on new trajectory")

        print(f"Robot position {query['position']}")
        print(f"Target position {query['target']}")

        print("Sending back next control input")
        socket.send_json([random() for _ in range(query['d_control'])])
