FROM node:16.13-bullseye-slim AS build

WORKDIR /app

RUN mkdir /root/.cache

COPY ./src/package*.json ./

RUN chown -R node:node /root

USER node

RUN npm install

COPY ./src ./

RUN npm run build


FROM nginx:1.20-alpine

COPY --from=build /app/dist /usr/share/nginx/html

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

COPY ./src/entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
