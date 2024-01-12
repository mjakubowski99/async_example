FROM python:3.10.11

ARG USER=${USER}
ARG UID=${UID}
ARG GID=${GID}

EXPOSE 80

RUN addgroup $USER --gid $GID
RUN useradd -rm -d /home/$USER -s /bin/bash -g $USER -G sudo -u $UID $USER

WORKDIR /run
COPY Pipfile Pipfile

RUN pip install uvicorn
RUN pip install --upgrade pip && pip install pipenv && pipenv lock && pipenv requirements > requirements.txt && pip install -r requirements.txt
RUN pip install pytest

RUN chown -R $USER:$USER /run

USER $USER

CMD ["/bin/bash"]