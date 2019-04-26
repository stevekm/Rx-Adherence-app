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
            axios.get("https://1eea6d14-23e6-4fc9-ba35-57f8f24e261d.mock.pstmn.io/users/").then(response => this.users=response.data.users)
        }
    }
</script>

<style scoped>

</style>