library(jsonlite)
library(rzmq)

context = init.context()
socket = init.socket(context,"ZMQ_REP")
bind.socket(socket,"ipc://socket")

print("This is the R controller")

while (TRUE) {
    query = fromJSON(rawToChar(receive.socket(socket, unserialize=FALSE)));
    # query$system    – robot name
    # query$init      – new robot/trajectory? true/false
    # query$d_control – length of required input control
    # query$state     – system state variables
    #                   (same order as the columns in the training data,
    #                    X, Y, Xi, Yi, ..., dX, dY, dXi, dYi, ...)
    # query$position  – x,y coordinates current position
    #                   (same as first two elements of query$state)
    # query$target    – x,y coordinates of next target position

    if (query$init) {
        print(paste("Initialise controller for",
                    query$system,
                    "on new trajectory"))
    }

    print(c("Robot position", query$position))
    print(c("Target position", query$target))

    print("Sending back next control input")
    send.socket(socket,
                charToRaw(toJSON(runif(query$d_control))),
                serialize=FALSE)
}
