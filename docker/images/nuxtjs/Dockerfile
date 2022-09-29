FROM debian:11

EXPOSE 3000

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install wget curl sudo xz-utils build-essential gcc zlib1g-dev

# FOR ARM
RUN wget https://nodejs.org/dist/v16.14.2/node-v16.14.2-linux-arm64.tar.xz -P /tmp ; mkdir /usr/local/lib/nodejs ; tar xvf /tmp/node-v16.14.2-linux-arm64.tar.xz  -C /tmp ; mv /tmp/node-v16.14.2-linux-arm64 /usr/local/lib/nodejs/
RUN rm -rf /usr/bin/node ; rm -rf  /usr/bin/npm ; rm -rf  /usr/bin/npx
RUN sudo ln -s /usr/local/lib/nodejs/node-v16.14.2-linux-arm64/bin/node /usr/bin/node ; sudo ln -s /usr/local/lib/nodejs/node-v16.14.2-linux-arm64/bin/npm /usr/bin/npm ; sudo ln -s /usr/local/lib/nodejs/node-v16.14.2-linux-arm64/bin/npx /usr/bin/npx

# FOR AMD64
# RUN wget https://nodejs.org/dist/v16.15.0/node-v16.15.0-linux-x64.tar.xz -P /tmp ; mkdir /usr/local/lib/nodejs ; tar xvf /tmp/node-v16.15.0-linux-x64.tar.xz  -C /tmp ; mv /tmp/node-v16.15.0-linux-x64 /usr/local/lib/nodejs/
# RUN rm -rf /usr/bin/node ; rm -rf  /usr/bin/npm ; rm -rf  /usr/bin/npx
# RUN sudo ln -s /usr/local/lib/nodejs/node-v16.15.0-linux-x64/bin/node /usr/bin/node ; sudo ln -s /usr/local/lib/nodejs/node-v16.15.0-linux-x64/bin/npm /usr/bin/npm ; sudo ln -s /usr/local/lib/nodejs/node-v16.15.0-linux-x64/bin/npx /usr/bin/npx

# INSTALL PYTHON FOR NODEJS PACKAGES
RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz -P /tmp ; tar xzf /tmp/Python-3.9.1.tgz -C /tmp ; cd /tmp/Python-3.9.1/ ; ./configure --enable-optimizations ; make -j 2 ; cd  /tmp/Python-3.9.1 ; make install

WORKDIR /var/www

# CMD npm run generate && npm run start
CMD npm run dev