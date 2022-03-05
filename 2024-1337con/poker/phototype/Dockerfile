FROM node:12.18.1

#RUN useradd --user-group --system --create-home --no-log-init app
# USER app

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install

COPY . .

EXPOSE 3022

RUN echo '1337con{fake_flag_for_testing}' > /flag.txt
RUN chmod 0555 /flag.txt

RUN useradd --user-group --system --create-home --no-log-init app
USER app

ENTRYPOINT ["npm", "start"]
