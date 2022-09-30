<template>
    <div v-if="user" class="user">
        <h1>Welcome back {{ user.email }}</h1>
    </div>
</template>

<script>
export default {
    data() {
        return {};
    },
    props: ["user"],
};
</script>