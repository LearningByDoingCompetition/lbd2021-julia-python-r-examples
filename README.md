# Submission examples for Track ROBO of the [Learning By Doing – NeurIPS 2021 Competition](https://learningbydoingcompetition.github.io/)

MWEs (Minimal working examples) of Julia / Python / R docker images
and corresponding submissions for Track ROBO of the
[Learning By Doing – NeurIPS 2021 Competition](https://learningbydoingcompetition.github.io/).

# Quick Start

1. Zip the contents of one of the folders [submission-julia](submission-julia), [submission-python](submission-python), or [submission-r](submission-r),
2. submit to the debug phase of Track ROBO on [codalab](https://competitions.codalab.org/competitions/33622#participate-submit_results), and
3. on codalab "View ingestion output log".

## BYOD – Build/Bring Your Own Docker

This repository holds dockerfiles that can serve as a starting point for your own Docker images:
1. copy and adapt the respective `docker-[LANGUAGE]/Dockerfile`
to include the extra software and packages you need
for your submission,
2. build and publish the docker image,
3. adapt the `submission-[LANGUAGE]/metadata` file to point to your docker image,
4. adapt the `submission-[LANGUAGE]/controller.[jl,py,R]` file to implement your controller,
5. pack the contents of `submission-[LANGUAGE]/` as a zip file, and
6. submit to Track ROBO on [codalab](https://competitions.codalab.org/competitions/33622#participate-submit_results).

## Example Dockerfiles

The dockerfiles
* [docker-julia/Dockerfile](docker-julia/Dockerfile)
* [docker-python/Dockerfile](docker-python/Dockerfile)
* [docker-r/Dockerfile](docker-r/Dockerfile)

specify Ubuntu-based docker images for the respective programming languages
and include a minimal set of packages
to support the required [ZMQ](https://zeromq.org) socket IPC interface
between the evaluation programme and your participant controller container.

The MWE docker images are available on dockerhub
* [lbd2021-julia-example](https://hub.docker.com/r/learningbydoingdocker/lbd2021-julia-example)
* [lbd2021-python-example](https://hub.docker.com/r/learningbydoingdocker/lbd2021-python-example)
* [lbd2021-r-example](https://hub.docker.com/r/learningbydoingdocker/lbd2021-r-example)

## Example Submissions

The folders
* [submission-julia](submission-julia)
* [submission-python](submission-python)
* [submission-r](submission-r)

contain MWE of how to implement a controller that correctly interfaces
with the codalab evaluation programme.

## Mockrun

With `python3 mockrun.py julia`, `python3 mockrun.py python`,
or `python3 mockrun.py r`,
you can mock run one of the provided example submissions.
Here, `mockrun.py` acts as a dummy evaluation programme
to illustrate the query-response communication between the codalab evaluation programme
and your participant controller submissions (`controller.jl`, `controller.py`, `controller.R`).
The `requirements.txt` need to be installed for the mock run to work;
the requirements for the respective sample solutions need to be installed as well.

### julia

Requires julia with packages `ZMQ` and `JSON`.

```
$ python3 mockrun.py julia
Starting controller ./submission-julia/start.sh
Waiting for controller to start
This is the Julia controller
Controller started
Initialising robot-A on new trajectory
Querying controller for next control input for robot-A
Initialising controller for robot-A on new trajectory
Robot position Any[0.8254505995153694, 0.9490876806227335]
Target position Any[0.668885973068748, 0.667524561316813]
Sending back next control input
Received control input of correct length (3)
Querying controller for next control input for robot-A
Robot position Any[0.6853845995481772, 0.4441623654146012]
Target position Any[0.913458352990904, 0.6128784318086193]
Sending back next control input
Received control input of correct length (3)
Querying controller for next control input for robot-A
Robot position Any[0.2737516769673213, 0.6135752609551967]
Target position Any[0.23096663295665398, 0.20520552282984184]
Sending back next control input
Received control input of correct length (3)
Initialising robot-B on new trajectory
Querying controller for next control input for robot-B
Initialising controller for robot-B on new trajectory
Robot position Any[0.2210401866361854, 0.9250507537472914]
Target position Any[0.3464530011473529, 0.8495610201942656]
Sending back next control input
Received control input of correct length (5)
Querying controller for next control input for robot-B
Robot position Any[0.5925573165962547, 0.2891881603259173]
Target position Any[0.7716482170509573, 0.3428408033054722]
Sending back next control input
Received control input of correct length (5)
Querying controller for next control input for robot-B
Robot position Any[0.2754602115290796, 0.8249594358191383]
Target position Any[0.20710825796782073, 0.6185746496383506]
Sending back next control input
Received control input of correct length (5)
Completed mockrun
```

### python

Requires python3 with `pyzmq`.

```
$ python3 mockrun.py python
Starting controller ./submission-python/start.sh
Waiting for controller to start
This is the Python controller
Controller started
Initialising robot-A on new trajectory
Querying controller for next control input for robot-A
Initialising controller for robot-A on new trajectory
Robot position [0.3128713634619642, 0.942860478777962]
Target position [0.2650933049341305, 0.037196143486136646]
Sending back next control input
Received control input of correct length (3)
Querying controller for next control input for robot-A
Robot position [0.45149439016143056, 0.8156497746521103]
Target position [0.45479412158279775, 0.8348446345527175]
Sending back next control input
Received control input of correct length (3)
Querying controller for next control input for robot-A
Robot position [0.8658674398417644, 0.45702683664573795]
Target position [0.21498610002651897, 0.9051808944323616]
Sending back next control input
Received control input of correct length (3)
Initialising robot-B on new trajectory
Querying controller for next control input for robot-B
Initialising controller for robot-B on new trajectory
Robot position [0.4850742495362401, 0.5088916447736227]
Target position [0.38240970435582977, 0.6394796249499376]
Sending back next control input
Received control input of correct length (5)
Querying controller for next control input for robot-B
Robot position [0.29534139029179507, 0.5716848507718046]
Target position [0.5316744817034484, 0.5266538467620896]
Sending back next control input
Received control input of correct length (5)
Querying controller for next control input for robot-B
Robot position [0.05168237331565395, 0.13756592891491326]
Target position [0.9143765398567542, 0.3152200464454734]
Sending back next control input
Received control input of correct length (5)
Completed mockrun
```

### r

Requires r-base with `rzmq` and `jsonlite`.

```
$ python3 mockrun.py r
Starting controller ./submission-r/start.sh
Waiting for controller to start
[1] "This is the R controller"
Controller started
Initialising robot-A on new trajectory
Querying controller for next control input for robot-A
[1] "Initialise controller for robot-A on new trajectory"
[1] "Robot position"    "0.13179380463971"  "0.730246936026655"
[1] "Target position"   "0.451181405232111" "0.633057598504208"
[1] "Sending back next control input"
Received control input of correct length (3)
Querying controller for next control input for robot-A
[1] "Robot position"     "0.0756416385645416" "0.762634980720846"
[1] "Target position"   "0.761330829225643" "0.834429423353697"
[1] "Sending back next control input"
Received control input of correct length (3)
Querying controller for next control input for robot-A
[1] "Robot position"    "0.772920352019809" "0.35228269433828"
[1] "Target position"    "0.677901076150458"  "0.0186395706326338"
[1] "Sending back next control input"
Received control input of correct length (3)
Initialising robot-B on new trajectory
Querying controller for next control input for robot-B
[1] "Initialise controller for robot-B on new trajectory"
[1] "Robot position"    "0.288873556154727" "0.19630248455829"
[1] "Target position"   "0.818270129676716" "0.467905729178425"
[1] "Sending back next control input"
Received control input of correct length (5)
Querying controller for next control input for robot-B
[1] "Robot position"    "0.560540878379536" "0.3072572657889"
[1] "Target position"    "0.0738841555489663" "0.946871018814558"
[1] "Sending back next control input"
Received control input of correct length (5)
Querying controller for next control input for robot-B
[1] "Robot position"    "0.847871101390822" "0.138635583627623"
[1] "Target position"    "0.926567628733439"  "0.0680884981108142"
[1] "Sending back next control input"
Received control input of correct length (5)
Completed mockrun
```
