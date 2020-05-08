FROM klakegg/hugo:0.70.0-onbuild AS build

FROM nginx:alpine
COPY --from=build /target /usr/share/nginx/html
