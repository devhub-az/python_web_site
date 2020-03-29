window.axios = require('axios');
window.Vue = require('vue');

Vue.component('index', require('./components/index').default);

if (document.getElementById('app')) {
    const app = new Vue({
        el: '#app',
    });
}