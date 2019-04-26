<template>
    <form action="">
        <div class="modal-card" style="width: auto">
            <header class="modal-card-head">
                <p class="modal-card-title">Login</p>
            </header>
            <section class="modal-card-body">

                <b-field label="Username">
                    <b-input
                            type="username"
                            :value="username"
                            placeholder="Your username"
                            required>
                    </b-input>
                </b-field>
            </section>
            <footer class="modal-card-foot">
                <button class="button" type="button" @click="$parent.close()">Close</button>
                <button class="button is-primary">Login</button>
            </footer>
        </div>
    </form>
</template>

<script>
    export default {
        name: "ModalForm",
        props: ['username'],
    }
</script>

<style scoped>

</style>