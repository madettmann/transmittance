# syntax=docker/dockerfile:1

FROM python:3.8

COPY requirements.txt /bin
COPY plot_transmittance.py /bin

ENV PATH="/app:${PATH}"

WORKDIR /app

RUN pip install -r /bin/requirements.txt

CMD ["/bin/plot_transmittance.py"]
ENTRYPOINT ["python"]