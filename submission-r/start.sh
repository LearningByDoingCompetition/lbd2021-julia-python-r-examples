#!/bin/bash

cd "$(dirname "$0")"

exec Rscript controller.R
