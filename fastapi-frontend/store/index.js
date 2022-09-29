export const state = () => ({
    user: null,
    base_url: "http://localhost:80/",
});
  
export const actions = {
    async getUser({ state }) {
        await this.$axios.get(state.base_url + "user", {}, { headers: {"Access-Control-Allow-Origin": "*"} }).then((ret) => {
            state.user = ret;
        });
    }
}