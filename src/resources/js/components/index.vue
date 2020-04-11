<template>
    <div class="post-content" style="font-size: 20px">
        <div v-if="postsNotEmpty">
            <div class="post-content__item" v-for="post in posts">
                <header class="post__meta">
                    <a v-bind:href="'/users/@' + post.author" class="post__user-info user-info"
                       title="Paylaşmanın müəllifi">
                        <img
                             height="32" width="32"
                             alt="user avatar" class="user__avatar lazyload">
                        <span class="user-info__nickname user-info__nickname_small">Author</span>
                    </a>
                </header>
                <div class="post-content__header">
                    <a :href="'/post/' + post.id" class="post-title">
                        <h3>{{ post.name }}</h3>
                    </a>
                </div>
                <div class="post-content__body" v-html="post.body">
                </div>
            </div>
            <pagination v-if="pagination.last_page > 1" :pagination="pagination" :offset="5"
                        @paginate="getPosts()"/>
        </div>
    </div>
</template>

<script>

    export default {
        data: function () {
            return {
                posts: [],
                id: [],
                content: '',
                error: false,
                loading: false,
                hovered: false,
                postsNotEmpty: false,
                pagination: {
                    'current_page': 1
                },
            }
        },
        async created() {
            await this.getPosts();
        },
        methods: {
            async getHubPosts() {
                this.posts = this.hub;
            },
            async getPosts() {
                this.loading = true;
                await axios.get('/api/posts/?format=json' + '&page=' + this.pagination.current_page).then(response => {
                    this.loading = false;
                    if (response.data.data.length !== 0) {
                        this.posts = response.data.data;
                        this.pagination = response.data.meta;
                        if (this.pagination.last_page > 50) {
                            this.pagination.last_page = 50;
                        }
                        this.postsNotEmpty = true;
                        for (let i = 0; i < this.posts.length; i++) {
                            this.id[i] = this.posts[i].id;
                        }
                    }
                })
                    .catch(error => {
                        this.loading = false
                        this.error = true
                        // DEVELOPING PART
                        if (error.response) {
                            console.log(error.response.data);
                            console.log(error.response.status);
                            console.log(error.response.headers);
                        } else if (error.request) {
                            console.log(error.request);
                        } else {
                            console.log('Error', error.message);
                        }
                    });
            },
            async findVillainIdx(id) {
                let currindex = null;
                for (let i = 0; i < this.$data.posts.length; i++) {
                    if (id === this.$data.posts[i].data.id) {
                        currindex = i;
                        break;
                    }
                }
                return currindex;
            },
            async copy(id) {
                const link = window.location.origin + '/post/' + id;
                try {
                    this.$clipboard(link);
                    new Noty({
                        type: 'success',
                        text: '<div class="notification-image"><span class="mdi mdi-share"/></div> Link kopyalandi',
                    }).show();
                } catch (error) {
                }
            }
        },
    }
</script>
