# Use alpine Linux, download desired version of HUGO and build html files
FROM alpine:3.19.1 AS build
RUN apk add --no-cache wget=1.21.4-r0
ARG HUGO_VERSION="0.123.7"
ARG HUGO_ENV_ARG
WORKDIR /src
COPY ./ /src
RUN wget --quiet "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz" && \
    tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
    rm -r hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
    mv hugo /usr/bin && \
    chmod 755 /usr/bin/hugo && \
    mkdir /target && \
    hugo -d /target -e "${HUGO_ENV_ARG}"

# Serve the generated html using nginx
FROM nginxinc/nginx-unprivileged:alpine
RUN sed -i '3 a\    absolute_redirect off;' /etc/nginx/conf.d/default.conf && \
    sed -i '4 a\    add_header X-Frame-Options DENY always;' /etc/nginx/conf.d/default.conf && \
    sed -i 's/#error_page  404/error_page  404/' /etc/nginx/conf.d/default.conf
COPY --from=build /target /usr/share/nginx/html

EXPOSE 8080
