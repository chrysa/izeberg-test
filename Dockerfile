FROM python:3.11-alpine

ARG TARGET_FOLDER=/poke-izeberg-app

COPY src/ ${TARGET_FOLDER}/
COPY scripts/ /scripts

ENV PATH=${PATH}:/usr/bin/python:${TARGET_FOLDER} \
    PYTHONBREAKPOINT=ipdb.set_trace

WORKDIR ${TARGET_FOLDER}

RUN set -ex pipefail \
    && apk add --quiet --update --no-cache build-base linux-headers \
    && pip install --quiet --prefer-binary --upgrade --no-cache-dir pip \
    && pip install --quiet --prefer-binary --no-cache-dir .[production] \
    && mkdir -p /var/log/uwsgi /socket \
    && find /scripts -name "*.sh" -exec chmod +x {} \;

EXPOSE 8000

CMD ["/scripts/cmd.sh"]

HEALTHCHECK --interval=30s --timeout=30s --retries=10 --start-period=10s \
  CMD -f /socket/poke_izeberg.socket || exit 1
