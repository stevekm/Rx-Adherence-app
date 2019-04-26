<template>
    <section class="section">
        <div class="tabs">
            <ul class="has-text-dark">
                <li v-on:click="whichPage = 'Doctor'" v-bind:class="{'is-active':whichPage == 'Doctor'}">
                    <a>Prescriber</a>
                </li>
                <li v-on:click="whichPage = 'Patient'" v-bind:class="{'is-active':whichPage == 'Patient'}">
                    <a>Patient</a>
                </li>
                <li v-on:click="whichPage = 'About'" v-bind:class="{'is-active':whichPage == 'About'}">
                    <a>About</a>
                </li>
            </ul>
        </div>
    <div id="dashboard" class="container">

        <About v-if="whichPage=='About'"/>
        <Doctor v-else-if="whichPage=='Doctor'"/>
        <Patient v-else-if="whichPage=='Patient'"/>

<!--        <About/>-->
    </div>
    </section>
</template>

<script>
    import About from "./About";
    import Doctor from "./Doctor";
    import Patient from "./Patient";

    export default {
        name: "Dashboard",
        components: {
            About,
            Doctor,
            Patient
        },
        data: function() {
            return {
                whichPage: "Patient"
            }
        },
        methods: {
            updateSelected: function() {

            }
        }


    }
</script>

<style scoped>

</style>