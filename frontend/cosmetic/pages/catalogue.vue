<template>
    <main class="main">
        <div class="container">
            <div class="main-inner">
                <div class="main-aside">
                    <div class="main-category"><a href="">Главная</a><a href="">Каталог</a><a href="">Кремы</a></div>
                    <div class="main-filters">
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
                                        <input type="checkbox" name="option" value="Levrana" v-model="filters.brands">Levrana
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="Chocolatte" v-model="filters.brands">Chocolatte
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="ECOLAB" v-model="filters.brands">ECOLAB
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="Cafe_Mimi" v-model="filters.brands">Cafe Mimi
                                    </label>
                                </form>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Для кого</template>
                            <template v-slot:options>
                                <form>
                                    <label>
                                        <input @click='filters.who.push(...whoFull)' type="checkbox" name="option">Для всех
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="woman" v-model="filters.who">Для женщин
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="man" v-model="filters.who">Для мужчин
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="child" v-model="filters.who">Для детей
                                    </label>
                                </form>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Тип кожи</template>
                            <template v-slot:options>
                                <form>
                                    <label>
                                        <input @click='filters.derm.push(...dermFull)' type="checkbox" name="option">Для всех типов
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="dry" v-model="filters.derm">Для сухой
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="fat" v-model="filters.derm">Для жирной
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="old" v-model="filters.derm">Для зрелой
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="sens" v-model="filters.derm">Для чувствительной
                                    </label>
                                    <label>
                                        <input type="checkbox" name="option" value="comb" v-model="filters.derm">Для комбинированной
                                    </label>
                                </form>
                            </template>
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Средство для рук</template>
                            <!-- <template v-slot:options>
                                <AppFilterOption :model="customInput">
                                    <AppFilterInput
                                        v-for="input in arrOfInputs"
                                        :inputValue="input.value"
                                        :label="input.label"
                                        v-model="input.model"
                                    ></AppFilterInput>
                                </AppFilterOption>
                            </template> -->
                        </AppFilterField>
                        <AppFilterField>
                            <template v-slot:filter-name>Средство для тела</template>
                        </AppFilterField>
                        <!-- <AppCustomInput
                            v-model="customInput"
                            @update:modelCheck =
                        ></AppCustomInput> -->
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
    import { ref, watch, reactive, computed } from 'vue'

    const customInput = ref([]);
    watch (customInput, (cur, old) => {
        console.log(customInput);
    })
    const filters = reactive({ derm: [], brands: [], who: [], });
    const whoFull = [ "child", "man", "woman" ];
    const brandsFull = [ "Levrana", "Chocolatte", "Cafe_Mimi", "ECOLAB" ];
    const dermFull = [ "dry", "fat", "old", "sens", "comb" ];

    let whoAll = ref(false);
    let dermAll = ref(false);

    let derm = computed(() => {
        return filters.derm.length ? filters.derm : dermFull
    });
    let brands = computed(() => {
        return filters.brands.length ? filters.brands : brandsFull
    });
    let who = computed(() => {
        return filters.who.length ? filters.who : whoFull
    });
    watch(filters, () => {
        fetchApi().then(data => console.log(data));
    });

    const fetchApi = async () => {
        return useFetch(`http://127.0.0.1:8000/api/products/?d=${derm.value}&b=${brands.value}&w=${who.value}`, {
            onResponse ({ request, options, response}) {
                return response._data
            },
        })
    }
    // const arrOfInputs = [
    //     { label: 'Для всех типов', },
    //     { label: 'Для сухой', value: 'dry', model: customInput,},
    //     { label: 'Для жирной', value: 'fat', model: customInput,},
    //     { label: 'Для зрелой', value: 'old', model: customInput,},
    //     { label: 'Для чувствительной', value: 'sens', model: customInput,},
    //     { label: 'Для комбинированной', value: 'comb', model: customInput,},
    // ];
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