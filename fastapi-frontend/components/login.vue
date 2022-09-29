<template>
    <div class="content-login">
        <div class="center">
            <input type="email" v-model="email" placeholder="Email" maxlength="90"/>
            <input type="password" v-model="password" placeholder="Password" maxlength="35"/>
            <button @click="login()">Connexion</button>
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
        async login() {
            if (!this.email || !this.password)
                return;
            await this.$axios.post("http://api.fastapi.local/user/login", {email: this.email, password: this.password}).then((ret) => {
                console.log(ret);
            });
        }
    },
}
</script>