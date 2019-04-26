<template>
    <section>
    <User v-for="name in users" :Name="name"></User>
    </section>
</template>

<script>
    import axios from "axios";
    import User from "./User";

    export default {
        name: "Users",
        components: {
            User
        },
        data: function() {
            return {
            users: []
        }
        },
        mounted() {
            axios.get("http://127.0.0.1:8000/usages/").then(response => this.users=Object.values(response.data))
        }
    }
</script>

<style scoped>

</style>