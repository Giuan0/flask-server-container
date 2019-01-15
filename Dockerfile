FROM pytorch/pytorch

RUN apt update

RUN pip install Flask

COPY server.py /workspace

ENV FLASK_APP=/workspace/server.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000

CMD flask run --host=0.0.0.0 && /bin/bash