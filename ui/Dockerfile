FROM node:14

ENV HOST=0.0.0.0

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /container-ui

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . /container-ui/

# build app for production with minification
# RUN npm run build

# CMD [ "http-server", "dist" ]
CMD [ "npm", "run", "serve" ]

# RUN npm install nodemon
# CMD ["nodemon", "--ext", "js,css,vue", "--watch src", "--exec", "npm", "run", "serve" ]
