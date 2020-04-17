FROM node:alpine as build

COPY . /code
WORKDIR /code

RUN yarn install
RUN yarn build

FROM nginx:alpine

COPY --from=build /code/dist/ /usr/share/nginx/html/

COPY ./k8s/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
