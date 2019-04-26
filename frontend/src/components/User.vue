<template>
    <section>
        <b-collapse
                aria-id="contentIdForA11y2"
                class="panel"
                :open.sync="isOpen">
            <div
                    slot="trigger"
                    class="panel-heading"
                    role="button"
                    aria-controls="contentIdForA11y2">
                <strong>{{Name}}</strong>
            </div>
            <div class="panel-block  has-background-secondary">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. <br/>
                Nulla accumsan, metus ultrices eleifend gravida, nulla nunc varius lectus, nec rutrum justo nibh eu lectus. <br/>
                Ut vulputate semper dui. Fusce erat odio, sollicitudin vel erat vel, interdum mattis neque.
            </div>
        </b-collapse>

    </section>
</template>

<script>
    export default {
        name: "User",
        data() {
            return {
                isOpen: true
            }
        },
        props: {
            Name: {
                type: String,
                required: true
                // default: 'Lucas'
            }
        }
    }
</script>

<style scoped>

</style>