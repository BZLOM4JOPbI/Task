// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            charset: 'utf-8',
            viewport: 'width=device-width, initial-scale=1',
            link: [
                {
                  rel: 'preconnect',
                  href: 'https://fonts.googleapis.com'
                },
                {
                  rel: 'preconnect',
                  href: 'https://fonts.gstatic.com',
                  crossorigin: ''
                },
                {
                  rel: 'stylesheet',
                  href: 'https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&family=Raleway:wght@400;500;600&display=swap'
                },
                {
                    rel: 'stylesheet',
                    href: '/styles/style.css',
                    type: 'text/css'
                },
              ],
        }
    }
})
