FROM python:3.7.4 AS intermediate

# WORKDIR /src/test.py
# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt
    # pip install requests && \
    # pip install bs4

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


FROM node:latest
COPY app.js .
COPY package.json .
COPY --from=intermediate . .
RUN npm install


CMD [ "npm", "start" ]
