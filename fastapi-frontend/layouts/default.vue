<template>
    <main>
        <header>
            <nuxt-link to="#">Connexion</nuxt-link>
            <nuxt-link to="#">Inscription</nuxt-link>
        </header>
        <Nuxt/>
    </main>
</template>

<script>
export default {
    data() {
        return {};
    },
    async mounted() {
        await this.$store.dispatch("getUser");
    },
};
</script>
