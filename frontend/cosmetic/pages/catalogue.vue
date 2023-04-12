<template>
    <main class="main">
        <div class="container">
            <div class="main-inner">
                <div class="main-aside">
                    <div class="main-category"><a href="">Главная</a><a href="">Каталог</a><a href="">Кремы</a></div>
                    <div class="main-filters">
                        <div class="filter catalogue">
                            <img src="/img/icons/grid.svg" alt=""><span>Каталог</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Цена</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Бренды</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Для кого</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Тип кожи</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Средство для рук</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Средство для рук</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                        <div class="filter">
                            <span>Средство для тела</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                    </div>
                </div>
                <div class="main-list-cards">
                    <div class="main-header">
                        <h3 class="main-product">Кремы</h3>
                        <div class="filter">
                            <span>Упорядочить</span>
                            <img class='arrow' src="/img/icons/arrow.svg" alt="">
                        </div>
                    </div>
                    <div class="card-grid">
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                        <div class="card">
                            <img class='catd-img' src="/img/photo.png" alt="">
                            <h6 class="card-title">Payot cream — для всех типов кожи</h6>
                            <p class="card-desc">Женский крем</p>
                            <p class="card-price">590 ₽</p>
                            <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

</template>

<style scoped>
    .main {
        padding: 80px 0;
        flex: 1 1 auto;
    }
    .main-inner {
        display: flex;
    }
    .main-aside {
        width: 282px;
        margin-right: 30px;
        flex-shrink: 0;
    }
    .main-list-cards {
        width: 100%;
    }
    .main-category a {
        position: relative;
        margin-right: 30px;
    }
    .main-category a:last-child {
        margin-right: 0;
        color: var(--text-opacity);
    }
    .main-category a:nth-child(1)::before, .main-category a:nth-child(2)::before{
        content: '/';
        right: -20px;
        top: 0;
    }
    .main-category {
        margin: 22px 0 78px;
    }
    .filter {
        width: 100%;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        cursor: pointer;
        padding-right: 10px;
    }
    .arrow {
        /* justify-self: flex-end; */
        margin-left: auto;
    }
    .filter span {
        font-size: 18px;
        font-weight: 600;
    }
    .catalogue {
        background-color: var(--color-focus);
        padding: 20px 10px;
    }
    .catalogue img:first-child {
        margin-right: 10px;
    }
    .main-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 50px;
    }
    .main-header .filter{
        padding: 0;
        width: 145px;
    }
    .main-header .filter span {
        font-weight: 400;
    }
    .main-product {
        font-size: 52px;
        line-height: 70px;
        font-weight: 500;
        font-family: 'Montserrat Alternates', sans-serif;
    }
    .card {
        width: 282px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        position: relative;
    }
    .card-title {
        margin: 20px 0 5px;
        font-size: 20px;
        line-height: 26px;
        font-weight: 500;
        color: var(--color-accent);
    }
    .card-price {
        font-size: 20px;
        line-height: 26px;
        font-weight: 500;
        margin: 17px 0 12px;
    }
    .card-desc {
        color: var(--text-opacity);
    }
    .add-to-cart {
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: var(--color-accent);
        padding: 13px 20px;
        cursor: pointer;
    }
    .add-to-cart img {
        filter: invert(1);
    }
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(282px, 282px));
        grid-gap: 30px;
    }
</style>