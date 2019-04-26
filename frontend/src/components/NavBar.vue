<template>
    <div id="navbar">
        <nav class="navbar is-fixed-top is-primary" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="/">
                    <p><strong>Rx-Adherence</strong></p>
                </a>

                <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>

            <div id="navbarBasicExample" class="navbar-menu">
<!--                <div class="navbar-start">-->
<!--                    <a class="navbar-item">-->
<!--                        Home-->
<!--                    </a>-->

<!--                    <a class="navbar-item has-text-secondary">-->
<!--                        Doctor-->
<!--                    </a>-->
<!--                    <a class="navbar-item">-->
<!--                        Patient-->
<!--                    </a>-->

<!--                    <div class="navbar-item has-dropdown is-hoverable">-->
<!--                        <a class="navbar-link">-->
<!--                            More-->
<!--                        </a>-->

<!--                        <div class="navbar-dropdown">-->
<!--                            <a class="navbar-item">-->
<!--                                About-->
<!--                            </a>-->
<!--                            <a class="navbar-item">-->
<!--                                Jobs-->
<!--                            </a>-->
<!--                            <a class="navbar-item">-->
<!--                                Contact-->
<!--                            </a>-->
<!--                            <hr class="navbar-divider">-->
<!--                            <a class="navbar-item">-->
<!--                                Report an issue-->
<!--                            </a>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->

<!--                <div class="navbar-end">-->
<!--                    <div class="navbar-item">-->
<!--                        <div class="buttons">-->
<!--                            <button class="button is-small is-white">-->
<!--                                Sign up-->
<!--                            </button>-->
<!--                            <LoginModal/>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
            </div>
        </nav>
    </div>
</template>

<script>
    import LoginModal from "./LoginModal";

    export default {
        name: "NavBar",
        components: {
            LoginModal
        }
    }
</script>

<style scoped lang="scss">

</style>