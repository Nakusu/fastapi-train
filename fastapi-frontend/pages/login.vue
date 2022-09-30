<template>
    <div class="content-login">
        <div v-if="!getUser" class="center">
            <input type="email" v-model="email" placeholder="Email" maxlength="90"/>
            <input type="password" v-model="password" placeholder="Password" maxlength="35"/>
            <button @click="login()">Connexion</button>
        </div>
        <div v-else class="center">
            <user :user="getUser"/>
        </div>
    </div>
</template>

<script>
import user from '~/components/user.vue';
export default {
  components: { 
      user 
    },
    data() {
        return {
            email: null,
            password: null
        };
    },
    computed: {
        getUser() {
            return this.$store.state.user;
        }
    },
    methods: {
        async login() {
            if (!this.email || !this.password || this.password.length < 3 || this.email.length < 3)
                return alert("Bad inputs!");
            await this.$axios.post("http://api.fastapi.local/user/login", {email: this.email, password: this.password}, {withCredentials: true}).then((ret) => {
                alert(ret.data);
                this.$store.dispatch("getUser");
            }).catch(err => {
            });
        }
    },
}
</script>