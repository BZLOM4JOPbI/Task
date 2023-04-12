<template>
    <header class="header">
        <div class="container">
            <div class="header-inner">
                <div class="header-links">
                    <a href=""><img src="/img/Logo.svg" alt="Logo" class="logo"></a>
                    <a href="">Каталог</a>
                    <a href="">Бренды</a>
                    <a href="">Акции</a>
                    <a href="">О компании</a>
                    <a href="">Контакты</a>
                </div>
                <div class="header-menu">
                    <a href=""><img src="/img/Icons.svg" alt=""></a>
                    <a href=""><img src="/img/Icons-1.svg" alt=""></a>
                    <a href=""><img src="/img/Icons-2.svg" alt=""></a>
                </div>
            </div>
        </div>
    </header>
</template>

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
</style>