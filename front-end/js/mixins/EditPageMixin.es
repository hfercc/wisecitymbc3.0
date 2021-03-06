export default {
    route: {
        data (transition) {
            let id = transition.to.params.id
            let config = this.$options.editConfig || {}

            if (!id) return transition.next()

            return this.$http.get(config.getInitURL(id))
                .then(res => ({
                    [config.objectFieldName]: res.data
                }))
        }
    },
}