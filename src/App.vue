<template>
<div id="app">
  <nav class="navbar is-light" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <div class="navbar-item">
        Swedish COVID-19 Data Hub
      </div>
      <a role="button"
         class="navbar-burger"
         aria-label="menu"
         aria-expanded="false"
         @click="showMenu = !showMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" id="navbarMenu" :class="{'navbar-menu': true, 'is-active': showMenu}">
      <div class="navbar-start"></div>
      <div class="navbar-end">
      <router-link to="/" class="navbar-item">
        Home
      </router-link>
      <router-link to="/about" class="navbar-item">
        About
      </router-link>
      <router-link to="/about" class="navbar-item">
        Datasets
      </router-link>
      <router-link to="/about" class="navbar-item">
        Support
      </router-link>
      </div>
    </div>
  </nav>

  <router-view class="container"></router-view>

  <footer class="footer">
    <a href="https://www.scilifelab.se/data/">
      <img class="logo" :src="require('./assets/img/data-centre-logo.svg')" alt="SciLife Data Centre logo"/>
    </a>
    <a href="https://www.nbis.se">
      <img class="logo" :src="require('./assets/img/nbislogo-orange-txt.svg')" alt="NBIS logo"/>
    </a>
    <a href="http://www.elixir-sweden.org">
      <img class="logo" :src="require('./assets/img/elixir-se-logo.png')" alt="NBIS logo"/>
    </a>
    <a href="https://www.vr.se">
      <img class="logo" :src="require('./assets/img/vr-logo-sve.svg')" alt="VR logo"/>
    </a>
  </footer>
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

img.logo {
    height: 70px;
    margin: 20px;
}
</style>
