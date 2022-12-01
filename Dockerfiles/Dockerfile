FROM klakegg/hugo:0.104.3-ubuntu-onbuild AS build

FROM nginxinc/nginx-unprivileged:alpine
RUN sed -i '3 a\    absolute_redirect off;' /etc/nginx/conf.d/default.conf
COPY --from=build /target /usr/share/nginx/html

EXPOSE 8080
