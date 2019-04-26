<template>
    <section>
        <button class="button is-white is-small"
                @click="isComponentModalActive = true">
            Sign in
        </button>

        <b-modal :active.sync="isComponentModalActive" has-modal-card>
            <modal-form v-bind="formProps"></modal-form>
        </b-modal>
    </section>
</template>

<script>

    import ModalForm from "./ModalForm";

    export default {
        name: "LoginModal",
        components: {
            ModalForm
        },
        data() {
            return {
                isComponentModalActive: false,
                formProps: {
                    email: 'username',
                }
            }
        }
    }
</script>

<style scoped>

</style>