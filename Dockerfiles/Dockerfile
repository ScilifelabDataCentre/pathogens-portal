FROM klakegg/hugo:0.91.2-onbuild AS build

FROM nginxinc/nginx-unprivileged:alpine
COPY --from=build /target /usr/share/nginx/html

EXPOSE 8080
