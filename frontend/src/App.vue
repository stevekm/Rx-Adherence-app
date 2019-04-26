<!--1eea6d14-23e6-4fc9-ba35-57f8f24e261d.mock.pstmn.io-->
<template>
  <div id="app" class="has-background-light has-text-dark">
      <Navbar/>
      <Dashboard/>
  </div>
</template>

<script>
import Navbar from "./components/NavBar";
import Dashboard from "./components/Dashboard";

export default {
  name: 'app',
  components: {
      Dashboard,
    Navbar,
  }
}
</script>

<style lang="scss">
    // Import Bulma's core
    @import "~bulma/sass/utilities/_all";

    // Set your colors
    $primary: #1a3c40;
    $primary-invert: findColorInvert($primary);
    $secondary: #e4eddb;
    $secondary-invert: findColorInvert($secondary);
    $twitter: #4099FF;
    $twitter-invert: findColorInvert($twitter);
    $light: #307672;
    $light-invert: findColorInvert($light);

    // Setup $colors to use as bulma classes (e.g. 'is-twitter')
    $colors: (
            "white": ($white, $black),
            "black": ($black, $white),
            "light": ($light, $light-invert),
            "dark": ($dark, $dark-invert),
            "primary": ($primary, $primary-invert),
            "secondary": ($secondary, $secondary-invert),
            "info": ($info, $info-invert),
            "success": ($success, $success-invert),
            "warning": ($warning, $warning-invert),
            "danger": ($danger, $danger-invert),
            "twitter": ($twitter, $twitter-invert)
    );

    // Links
    $link: $primary;
    $link-invert: $primary-invert;
    $link-focus-border: $primary;

    // Import Bulma and Buefy styles
    @import "~bulma";
    @import "~buefy/src/scss/buefy";
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #307672;
    margin-top: 60px;
}
    html {
        background: #307672;
    }
</style>
