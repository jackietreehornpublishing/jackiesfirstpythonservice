# Smallest base Python3.5 image available based on alpine
FROM frolvlad/alpine-python3
MAINTAINER russmiles <russ@russmiles.com>

COPY requirements/prod.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY mypackage/ /usr/local/atomist/mypackage

# this allows us to run the package as a native module below
COPY mypackage/main.py /usr/local/atomist/mypackage/__main__.py

COPY setup.py /usr/local/atomist
RUN cd /usr/local/atomist && pip install .

EXPOSE 8080

ENTRYPOINT [ "python3", "-m", "mypackage" ]
