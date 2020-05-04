# Covid-19 Hub

## Libraries

* [vue.js](https://vuejs.org) as frontend framework
* [bulma](https://bulma.io) is the CSS framework

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Running through docker

For setup/lint and build just prepend:

```
docker run -ti --rm -v "$PWD":/usr/src/app -w /usr/src/app node
```

to the yarn command, i.e.:

```
docker run -ti --rm -v "$PWD":/usr/src/app -w /usr/src/app node yarn install
```

### Compiles and hot-reloads for development

```
docker run --expose 8080 -p 8080:8080 --rm -ti -v $PWD:/usr/src/app -w /usr/src/app node yarn serve
```
