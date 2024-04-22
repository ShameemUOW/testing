FROM node:latest AS node_python_base

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN pip3 install pipx && pipx install mysql-connector-python

CMD ["npm", "start"]