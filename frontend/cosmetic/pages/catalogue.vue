<template>
    <main class="main">
        <div class="container">
            <div class="main-inner">
                <div class="main-aside">
                    <div class="main-category"><a href="">Главная</a><a href="">Каталог</a><a href="">Кремы</a></div>
                    <div class="main-filters">
                        <!-- <div> {{ filterListener }}</div> -->
                        <AppFilterCatalogue></AppFilterCatalogue>
                        <AppFilterField>
                            <template v-slot:filter-name>Цена</template>
                            <template v-slot:options>
                                <AppPriceRange></AppPriceRange>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Бренды</template>
                            <template v-slot:options>
                                <form>
                                    <label>
                                        <input type="checkbox" name="option" value="Levrana" v-model="brands">Levrana
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="Chocolatte" v-model="brands">Chocolatte
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="ECOLAB" v-model="brands">ECOLAB
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="Cafe_Mimi" v-model="brands">Cafe Mimi
                                    </label>
                                </form>
                                <div>{{ brands }}</div>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Для кого</template>
                            <template v-slot:options>
                                <form>
                                    <label>
                                        <input @click="selesctAlla" type="checkbox" name="option">Для всех
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allA" name="option" value="woman" v-model="who">Для женщин
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allA" name="option" value="man" v-model="who">Для мужчин
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allA" name="option" value="child" v-model="who">Для детей
                                    </label>
                                </form>
                                <div>{{ who }}</div>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Тип кожи</template>
                            <template v-slot:options>
                                <form>
                                    <label>
                                        <input type="checkbox" @click="selesctAllb" name="option">Для всех типов
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allB" name="option" value="dry" v-model="dermTypeFilter">Для сухой
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allB" name="option" value="fat" v-model="dermTypeFilter">Для жирной
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allB" name="option" value="old" v-model="dermTypeFilter">Для зрелой
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allB" name="option" value="sens" v-model="dermTypeFilter">Для чувствительной
                                    </label>
                                    <label>
                                        <input type="checkbox" v-bind:checked="allB"  name="option" value="comb" v-model="dermTypeFilter">Для комбинированной
                                    </label>
                                </form>
                                <div>{{ dermTypeFilter }}</div>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Средство для рук</template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Средство для тела</template>
                        </AppFilterField>
                        <div>
                            <AppFilterInput v-for="input in inputs" :label = "input.label" :value = "input.value"></AppFilterInput>
                        </div>
                    </div>
                </div>
                <div class="main-list-cards">
                    <div class="main-header">
                        <h3 class="main-product">Кремы</h3>
                        <AppOrderCatalogue></AppOrderCatalogue>
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
<script setup>
    import { ref, watch } from 'vue';

    const dermTypeFilter = ref([]);
    const brands = ref([]);
    const who = ref([]);
    const whoFull = [ "child", "man", "woman" ];
    const brandsFull = [ "Levrana", "Chocolatte", "Cafe_Mimi", "ECOLAB" ];
    const dermFull = [ "dry", "fat", "old", "sens", "comb" ];
    const refVar = ref('')
    const inputs = [ 
        { label: 'For human', 'v-model': 'someFilter', value: 'man', },
        { label: 'For woman', 'v-model': 'someFilter', value: 'woman', },
        { label: 'For little', 'v-model': 'someFilter', value: 'child', }
    ]

    let allA = ref(false);
    let allB = ref(false);

    watch (who, async (cur, old) => {
        console.log(who)
        fetchApi().then(data => console.log(data));
    })
    watch (dermTypeFilter, async (cur, old) => {
        fetchApi().then(data => console.log(data));
    })
    watch (brands, async (cur, old) => {
        fetchApi().then(data => console.log(data));
    })
    const fetchApi = async () => {
        return useFetch(`http://127.0.0.1:8000/api/products/?d=${dermTypeFilter.value.length ? dermTypeFilter.value : dermFull}&b=${brands.value.length ? brands.value : brandsFull}&w=${who.value.length ? who.value : whoFull}`, {
            onResponse ({ request, options, response}) {
                return response._data
            },
        })
    }
    const selectAlla = () => {
        allA.value = true;
    }
    const selectAllb = () => {
        allB.value = true;
    }
</script>
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
        justify-content: space-around;
    }
    label {
        margin-bottom: 10px;
        font-size: 18px;
        display: flex;
        align-items: center;
        width: 100%;
    }
    label input[type='checkbox'] {
        margin-right: 10px;
        position: relative;
        /* -moz-appearance:none;
        -webkit-appearance:none;
        -o-appearance:none; */
        width: 20px;
        height: 20px;
        accent-color: var(--color-accent);
        /* border: 1px solid var(--color-accent);  */
    } 
    form label:last-child {
        margin-bottom: 20px;
    }
</style>