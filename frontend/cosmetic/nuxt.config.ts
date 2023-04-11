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
                  rel: 'stylesheet',
                  href: 'https://fonts.googleapis.com/css2?family=Roboto&display=swap',
                  crossorigin: ''
                },
                {
                    rel: 'stylesheet',
                    href: '/styles/style.css',
                    type: 'text/css'
                }
              ],
        }
    }
})
