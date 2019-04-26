<template>
    <section>
        <p class="content"><b>Selected:</b> {{ selected }}</p>
        <b-field label="Enter Patient Name">
            <b-autocomplete
                    rounded
                    v-model="name"
                    :data="filteredDataArray"
                    placeholder="e.g. John"
                    icon="magnify"
                    @select="option => selected = option">
                <template slot="empty">No results found</template>
            </b-autocomplete>
        </b-field>
        <p class="content"><b>Selected:</b> {{ drugSelected }}</p>
        <b-field label="Enter Drug Name">
            <b-autocomplete
                    rounded
                    v-model="drug"
                    :data="filteredDrugDataArray"
                    placeholder="e.g. Drug Name"
                    icon="magnify"
                    @select="option => drugSelected = option">
                <template slot="empty">No results found</template>
            </b-autocomplete>
        </b-field>
    </section>
</template>

<script>
    import axios from "axios";

    export default {
        name: "Patient",
        data: function(){
            return {
                users: [],
                drugs: [],
                name: '',
                drug: '',
                drugSelected: null,
                selected: null
            }
        },
        mounted() {

            axios.get("http://127.0.0.1:8000/users/").then(response => this.users=Object.values(response.data));
            axios.get("http://127.0.0.1:8000/drugs/").then(response => this.drugs=Object.values(response.data));
            // axios.get("https://1eea6d14-23e6-4fc9-ba35-57f8f24e261d.mock.pstmn.io/drugs/").then(response => this.drugs=response.data.drugs.values);
        },
        computed: {
            filteredDataArray() {
                if (this.users.length > 0) {
                    return this.users.filter((option) => {
                        return option
                            .toString()
                            .toLowerCase()
                            .indexOf(this.name.toLowerCase()) >= 0
                    })
                } else {
                    return []
                }
            },
            filteredDrugDataArray() {
                if (this.drugs.length > 0) {
                    return this.drugs.filter((option) => {
                        return option
                            .toString()
                            .toLowerCase()
                            .indexOf(this.drug.toLowerCase()) >= 0
                    })
                } else {
                    return []
                }
            }
        }
    }
</script>

<style scoped>

</style>

module.exports = {
devServer: {proxy: 'http://localhost:3000'}
}