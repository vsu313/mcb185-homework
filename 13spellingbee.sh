#!/bin/bash

gunzip -c dictionary.gz | grep "r" | grep -v "[bdefghjklmpqrstuvwxy]"
