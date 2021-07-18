using JSON, ZMQ

s = Socket(REP)
bind(s, "ipc://socket")

println("This is the Julia controller")

while true
    query = JSON.parse(recv(s, String))
    # query["system"]    – robot name
    # query["init"]      – new robot/trajectory? true/false
    # query["d_control"] – length of required input control
    # query["state"]     – system state variables
    #                      (same order as the columns in the training data,
    #                       X, Y, Xi, Yi, ..., dX, dY, dXi, dYi, ...)
    # query["position"]  – x,y coordinates current position
    #                      (same as first two elements of query["state"])
    # query["target"]    – x,y coordinates of next target position

    if query["init"]
        println("Initialising controller for ",
                query["system"],
                " on new trajectory")
    end

    println("Robot position ", query["position"])
    println("Target position ", query["target"])

    println("Sending back next control input")
    send(s, JSON.json(rand(query["d_control"])))
end
