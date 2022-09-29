<template>
    <main>
        <header>
            <nuxt-link v-if="!getUser" to="/login">Connexion</nuxt-link>
            <nuxt-link v-if="!getUser" to="/register">Inscription</nuxt-link>
            <button @click="logout()" v-if="getUser" to="#">Logout</button>
        </header>
        <Nuxt/>
    </main>
</template>

<script>
export default {
    data() {
        return {};
    },
    computed: {
        getUser() {
            return this.$store.state.user;
        },
    },
    methods: {
        async logout() {
            await this.$axios.get("http://api.fastapi.local/user/logout", {withCredentials: true}).then((ret) => {
                alert(ret.data);
                this.$store.dispatch("getUser");
            });
        }
    },
    async mounted() {
        await this.$store.dispatch("getUser");
    },
};
</script>
