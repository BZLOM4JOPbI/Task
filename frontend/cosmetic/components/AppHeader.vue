<template>
    <header class="header">
        <div class="container">
            <div class="header-inner">
                <div class="header-links">
                    <a href=""><img src="/img/Logo.svg" alt="Logo" class="logo"></a>
                    <div class="hide">
                        <a href="">Каталог</a>
                        <a href="">Бренды</a>
                        <a href="">Акции</a>
                        <a href="">О компании</a>
                        <a href="">Контакты</a>
                    </div>
                </div>
                <div class="header-menu hide">
                    <a href=""><img src="/img/icons/search.svg" alt=""></a>
                    <a href=""><img src="/img/icons/account.svg" alt=""></a>
                    <a href=""><img src="/img/icons/cart.svg" alt=""></a>
                </div>
                <div v-if="!isMediaQuery" class="burger-btn" @click="isBurgerActive = !isBurgerActive">  
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    </header>
    <nav v-show="isBurgerActive">
        <div class="container">
            <div class="nav-inner">
                <div class="flex-col">
                    <a href="">Каталог</a>
                    <a href="">Бренды</a>
                    <a href="">Акции</a>
                    <a href="">О компании</a>
                    <a href="">Контакты</a>
                </div>
                <div class="burger-menu">
                    <a href=""><img src="/img/icons/search.svg" alt=""></a>
                    <a href=""><img src="/img/icons/account.svg" alt=""></a>
                    <a href=""><img src="/img/icons/cart.svg" alt=""></a>
                </div>
            </div>
        </div>
    </nav>
</template>
<script setup>
    import { ref } from 'vue';

    const isMediaQuery = ref(true);
    if (process.client) {
        const mediaQuery = window.matchMedia('screen and (max-width: 800px)');
        const hideFooterCol = (event) => {
            isMediaQuery.value = !event.matches;
        }
        mediaQuery.addEventListener('change', hideFooterCol);
        hideFooterCol(mediaQuery);
    }

    const isBurgerActive = ref(false);
</script>
<style scoped>
    .header {
        border-bottom: 1px solid var(--color-accent);
    }
    .header-inner {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 60px;
    }
    .header-links {
        display: flex;
        align-items: center;
    }
    .header-links a {
        margin-right: 40px;
    }
    .header-links a:last-child {
        margin: 0;
    }
    .header-menu a {
        margin-right: 20px;
    }
    .header-menu a:last-child {
        margin: 0;
    }
    .burger-btn {
        width: 60px;
        height: 60px;
        background-color: transparent;
        position: relative;
        cursor: pointer;
    }
    .burger-btn span {
        position: absolute;
        left: 0;
        width: 70%;
        height: 3px;
        background-color: var(--color-accent);
        border-radius: 2px;
    }
    .burger-btn span:nth-child(1) {
        top: 20%;
    }
    .burger-btn span:nth-child(2) {
        top: 50%;
        transform: translate(0, -50%);
    }
    .burger-btn span:nth-child(3) {
        bottom: 20%;
    }
    .nav-inner {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .flex-col {
        padding: 15px 0 20px;
        gap: 20px;
    }
    .flex-col a {
        text-align: center;
    }
    .burger-menu {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .burger-menu a {
        margin-right: 20px;
    }
    .burger-menu a:last-child {
        margin-right: 0px;
    }
    @media screen and (min-width: 800px) {
        nav {
            display: none;
        }
    }
    @media screen and (max-width: 800px) {
        .hide {
            display: none;
        }
    }
</style>