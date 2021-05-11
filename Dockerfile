FROM openmc/openmc:develop

RUN git clone --single-branch --branch master https://github.com/openmc-dev/data.git

