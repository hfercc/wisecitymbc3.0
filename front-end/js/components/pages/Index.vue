<template>
    <div>
        <vs-jumbotron fluid>
            <div class="col-md-8 col-sm-12">
                <h1 class="display-3">
                    WiseCity
                </h1>
            </div>
            <div class="col-md-4 col-sm-12" v-show="!$root.hasLogined">
                <login-form></login-form>
            </div>
        </vs-jumbotron>
    </div>
</template>

<script>
    import LoginForm from 'auth/LoginForm.vue'

    export default {
        components: {
            LoginForm
        }
    }
</script>