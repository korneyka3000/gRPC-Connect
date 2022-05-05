#!/bin/bash
python3 manage.py grpcrunserver --dev &
P1=$!
python3 manage.py runserver 0.0.0.0:8000 &
P2=$!
wait $P1 $P2