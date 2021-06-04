FROM klakegg/hugo:0.80.0-onbuild AS build

FROM nginx:1.21-alpine
COPY container/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /target /usr/share/nginx/html
