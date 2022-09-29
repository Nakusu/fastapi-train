<template>
    <div class="content-login">
        <div class="center">
            <input type="email" v-model="email" placeholder="Email" maxlength="90"/>
            <input type="password" v-model="password" placeholder="Password" maxlength="35"/>
            <button @click="register()">Inscription</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: null,
            password: null
        };
    },
    methods: {
        async register() {
            if (!this.email || !this.password)
                return;
            await this.$axios.post("http://api.fastapi.local/user/register", {email: this.email, password: this.password}, {withCredentials: true}).then((ret) => {
                alert(ret.data);
                this.$store.dispatch("getUser");
            });
        }
    },
}
</script>