<template>
    <div>
        <div v-if="$root.user" class="clearfix top-btn-group">
            <div class="col-xs-6">
                <vs-link link="/me/" title="个人主页" icon="user"></vs-link>
            </div>
            <div class="col-xs-6">
                <vs-link link="/logout/" title="退出" icon="sign-out"></vs-link>
            </div>
        </div>
        <div v-else class="clearfix">
            <vs-link link="/login/" title="登录" icon="sign-in"></vs-link>
        </div>
        <vs-list-group flush>
            <vs-list-group-item v-if="$root.perms.articles_article_add_">
                <vs-link link="/edit/articles/" title="撰写" icon="pencil"></vs-link>
            </vs-list-group-item>
        </vs-list-group>
        <vs-list-group flush>
            <vs-list-group-item>
                <vs-expansion title="文章">
                    <vs-list-group flush slot="content">
                        <vs-list-group-item
                            v-for="category in categories">
                            <vs-link
                                :link="`/articles/${$key}/`"
                                :title="category">
                            </vs-link>
                        </vs-list-group-item>
                    </vs-list-group>
                </vs-expansion>
            </vs-list-group-item>
            <vs-list-group-item>
                <vs-expansion title="标签">
                    <vs-list-group flush slot="content">
                        <vs-list-group-item
                            v-for="tag in tags">
                            <vs-link
                                :link="tag.url"
                                icon="tag"
                                :title="tag.name">
                            </vs-link>
                        </vs-list-group-item>
                    </vs-list-group>
                </vs-expansion>
            </vs-list-group-item>
            <vs-list-group-item>
                <vs-link link="/companies/" title="公司"></vs-link>
            </vs-list-group-item>
            <vs-list-group-item>
                <vs-link link="/finance/" title="交易"></vs-link>
            </vs-list-group-item>
            <vs-list-group-item>
                <vs-link link="/ram/" title="能源及原材料"></vs-link>
            </vs-list-group-item>
            <vs-list-group-item>
                <vs-link link="/topics/" title="Q&amp;A"></vs-link>
            </vs-list-group-item>
        </vs-list-group>
    </div>
</template>

<style scoped>
    .top-btn-group {
        margin-bottom: 0.9375rem;
    }
</style>

<script>
    import { AVAILABLE_CATEGORIES } from 'consts.es'
    const CATEGORIES_NAME = ['政府', '公司', '媒体', '交易', '能源及原材料']

    export default {
        data: () => ({
            categories: _.zipObject(AVAILABLE_CATEGORIES, CATEGORIES_NAME),
            tags: []
        }),
        methods: {
            tagToggled () {
                this.$http.get('/api/tags/')
                    .then(res => this.tags = res.data.results )
            }
        },
        ready () {
            this.$http.get('/api/tags/', { params: {limit: 5}})
                .then(res => this.tags = res.data.results )
        },
        events: {
            ['BlockA:click'] () {
                this.$root.showSideBar = false
            }
        }
    }
</script>