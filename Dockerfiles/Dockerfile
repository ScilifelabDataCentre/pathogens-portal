FROM klakegg/hugo:0.91.2-onbuild AS build

FROM nginx:alpine
COPY Dockerfiles/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /target /usr/share/nginx/html
