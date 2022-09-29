export const state = () => ({
    user: null,
});
  
export const mutations = {
    async setUser(state, user) {
        state.user = user;
    }, 
};

export const actions = {
    async getUser({ commit }) {
        await this.$axios.get("http://api.fastapi.local/user", {withCredentials: true}).then((ret) => {
            commit("setUser", ret.data.status_code === 401 ? null : ret.data);
        }).catch((err) => {
            if (err.code === 401)
                return;
        });
    }
};