#!/bin/bash

cd "$(dirname "$0")"

exec julia controller.jl
