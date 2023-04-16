<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-inner">
                <div class="footer-up" v-if="flag">
                    <div class="footer-col">
                        <img src="/img/LogoWhite.svg" alt="Logo" class="logo">
                        <p>г. Воронеж, ул. Катукова, д. 37</p>
                    </div>
                    <div class="footer-col">
                        <p class="footer-col-head">Каталог</p>
                        <a class='footer-link' href="">Женские ароматы</a>
                        <a class='footer-link' href="">Мужские ароматы</a>
                        <a class='footer-link' href="">Акции</a>
                        <a class='footer-link' href="">Бренды</a>
                    </div>
                    <div class="footer-col">
                        <p class="footer-col-head">Бренды</p>
                        <a class='footer-link' href="">Levrana</a>
                        <a class='footer-link' href="">Chocolatte</a>
                        <a class='footer-link' href="">ECOLAB</a>
                        <a class='footer-link' href="">Cafe Mimi</a>
                    </div>
                    <div class="footer-col">
                        <p class="footer-col-head">О компании</p>
                        <a class='footer-link' href="">Информация</a>
                        <a class='footer-link' href="">Контакты</a>
                        <a class='footer-link' href="">Оптовое сотрудничество</a>
                    </div>
                    <div class="footer-col">
                        <p class="footer-col-head">Доставка и оплата</p>
                        <a href="" class="phone">8 (999) 770 38 93</a>
                        <div class="footer-socials">
                            <a class='social' href=""><img src="/img/socials/vk.svg" alt=""></a>
                            <a class='social' href=""><img src="/img/socials/tg.svg" alt=""></a>
                            <a class='social' href=""><img src="/img/socials/inst.svg" alt=""></a>
                            <a class='social' href=""><img src="/img/socials/whatsup.svg" alt=""></a>
                        </div>
                    </div>
                </div>
                <div class="footer-up" v-else>
                    <div>
                        <AppFilterField>
                            <template v-slot:filter-name>Каталог</template>
                            <template v-slot:options>
                                <a class='footer-link' href="">Женские ароматы</a>
                                <a class='footer-link' href="">Мужские ароматы</a>
                                <a class='footer-link' href="">Акции</a>
                                <a class='footer-link' href="">Бренды</a>
                            </template>
                        </AppFilterField>
                    </div>
                    <div>
                        <AppFilterField>
                            <template v-slot:filter-name>Бренды</template>
                            <template v-slot:options>
                                <a class='footer-link' href="">Levrana</a>
                                <a class='footer-link' href="">Chocolatte</a>
                                <a class='footer-link' href="">ECOLAB</a>
                                <a class='footer-link' href="">Cafe Mimi</a>
                            </template>
                    </AppFilterField>
                    </div>
                    <div>
                        <AppFilterField>
                            <template v-slot:filter-name>О компании</template>
                            <template v-slot:options>
                                <a class='footer-link' href="">Информация</a>
                                <a class='footer-link' href="">Контакты</a>
                                <a class='footer-link' href="">Оптовое сотрудничество</a>
                            </template>
                    </AppFilterField>
                    </div>
                    <div>
                        <AppFilterField>
                            <template v-slot:filter-name>Доставка и оплата</template>
                            <template v-slot:options>                        
                                <a href="" class="phone">8 (999) 770 38 93</a>
                                <div class="footer-socials">
                                    <a class='social' href=""><img src="/img/socials/vk.svg" alt=""></a>
                                    <a class='social' href=""><img src="/img/socials/tg.svg" alt=""></a>
                                    <a class='social' href=""><img src="/img/socials/inst.svg" alt=""></a>
                                    <a class='social' href=""><img src="/img/socials/whatsup.svg" alt=""></a>
                                </div>
                            </template>
                    </AppFilterField>
                    </div>
                    <p><img src="/img/LogoWhite.svg" alt="Logo" class="logo">г. Воронеж, ул. Катукова, д. 37</p>
                </div>
                <div class="footer-down">
                    <h6>© {{ currentYear }} SV Parfums & cosmetic</h6>
                </div>
            </div>
        </div>
    </footer>
</template>
<script setup>
    import { ref } from 'vue'

    const currentYear = new Date().getFullYear();

    const flag = ref(false);
    if (process.client) {
        const mediaQuery = window.matchMedia('screen and (max-width: 800px)');
        const hideFooterCol = (event) => {
            flag.value = !event.matches;
            console.log(flag.value);
        }
        mediaQuery.addEventListener('change', hideFooterCol);
        hideFooterCol(mediaQuery);
    }
</script>
<style scoped>
    * {
        color: var(--text-accent);
    }
    .footer {
        background-color: var(--color-accent);
        padding-bottom: 41px;
    }
    .footer-col {
        width: 200px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-right: 30px;
    }
    .footer-up .footer-col:first-child {
        width: 282px
    }
    .footer-col .footer-col-head{
        margin-bottom: 20px;
        font-size: 18px;
        line-height: 20px;
        font-weight: 600;
    }
    .footer-socials .social {
        margin-right: 24px;
    }
    .footer-socials .social:last-child {
        margin: 0;
    }
    .footer-col .footer-link {
        margin-bottom: 16px;
    }
    .phone {
        margin-bottom: 34px;
        font-weight: 500;
        font-size: 20px;
        line-height: 26px;
    }
    .footer-up {
        padding: 70px 0;
        display: flex;
        align-items: flex-start;
    } 

    .footer-down{ 
        padding-top: 30px;
        border-top: 1px solid var(--text-accent);
    }
    .footer-down h6 {
        font-size: 16px;
        color: var(--text-opacity);
        text-align: center;
        font-weight: 400;
    }
    .footer-link {
        margin-bottom: 10px;
        display: block;
    }
    /* .footer-filter-header {
        color: var(--text-accent);
    } */
    @media screen and (max-width: 950px) {
        .footer-col {
            margin-right: 20px;
        }
    }
    @media screen and (max-width: 800px) {
        .footer-up {
            display: grid;
            grid-template-columns: 1fr, 1fr;
            grid-gap: 50px;
            padding: 70px 20px;
        }
        .footer-link, .phone {
            color: rgb(19, 18, 18);
        }
        .social {
            filter: invert(1);
        }
        .footer-up > div {
            filter: invert(1);
        }
        p {
            grid-column: span 2;
            text-align: center;
        }
        p img {
            margin: 0 auto;
        }
    }
    @media screen and (max-width: 470px) {
        .footer-up {
            grid-gap: 25px;
            padding: 70px 0;
        }
    }
    @media screen and (max-width: 385px) {
        .footer-up > div {
            grid-column: span 2;
        }
        .social, .footer-link, .phone {
            padding-left: 15px;
        }
    }
</style>