<template>
    <section>
        <table class="table">
            <tr>
                <th>Drug</th>
                <th>Time</th>
            </tr>
            <tr v-for="name in info">
                <td>{{name.drug}}</td>
                <td>{{name.time}}</td>
            </tr>
        </table>
    </section>
    
</template>

<script>
    import axios from "axios";
    export default {
        name: "Table",
        data: function() {
            return {
                info: []
            }
        },
        props: {
            name: {
                type: String,
                required: true
                // default: 'Lucas'
            },
            drugId: {
                type: String,
                required: true
            }
        },
        watch: {
            // name: function () {
            //     let query = "http://127.0.0.1:8000/usages/" + this.name + '/' + this.drugId;
            //     axios.get(query).then(response => this.info = response.data);
            //     // axios.get("https://1eea6d14-23e6-4fc9-ba35-57f8f24e261d.mock.pstmn.io/drugs/").then(response => this.drugs=response.data.drugs.values);
            // },

            drugId: function () {
                let query = "http://127.0.0.1:8000/usages/" + this.name + '/' + this.drugId;
                axios.get(query).then(response => this.info = response.data);
                // axios.get("https://1eea6d14-23e6-4fc9-ba35-57f8f24e261d.mock.pstmn.io/drugs/").then(response => this.drugs=response.data.drugs.values);
            }
        }
    }
</script>

<style scoped>

</style>