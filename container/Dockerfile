FROM klakegg/hugo:0.78.2-onbuild AS build

FROM nginx:alpine
COPY container/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /target /usr/share/nginx/html
