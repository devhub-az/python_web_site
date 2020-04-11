window.axios = require('axios');
window.Vue = require('vue');

Vue.component('index', require('./components/index').default);
Vue.component('pagination', require('./components/plugins/pagination').default);

Vue.config.productionTip = false;
Vue.config.silent = false;
Vue.config.keyCodes.backspace = 8;
Vue.config.devtools = false

if (document.getElementById('app')) {
    const app = new Vue({
        el: '#app',
    });
}