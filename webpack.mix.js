let mix = require('laravel-mix');

let staticPath = 'blog/static/'
let resourcesPath = 'resources'

mix.setResourceRoot('/static/build') // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg

mix.setPublicPath('blog/static') // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}

// Now you can use full mix api
mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/js`)
mix.sass(`${resourcesPath}/scss/app.scss`, `${staticPath}/css`)

mix.disableNotifications()
    .sourceMaps()