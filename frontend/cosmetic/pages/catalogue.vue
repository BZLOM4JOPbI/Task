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
                                <!-- <AppPriceRange></AppPriceRange> -->
                                <div class="price-range">
                                    <p class="display-range">{{ filters.minValue }} - {{ filters.maxValue }}</p>
                                    <input type="range" min="350" max="5000" step="50" :value="filters.minValue" @change="bindMinValue">
                                    <input type="range" min="350" max="5000" step="50" :value="filters.maxValue" @change="bindMaxValue">
                                </div>
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
                                        <input @change='fillFilter' value='who' type="checkbox" name="option">Для всех
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
                                        <input @change='fillFilter' type="checkbox" value='derm' name="option">Для всех типов
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
                        <AppCard v-for="card in cards"
                            :title="card.title_of_product"
                            :desc="card.brief_info_about_product"
                            :price="card.price"></AppCard>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
<script setup>
    import { ref, watch, reactive, computed, onMounted } from 'vue'

    const filters = reactive({ derm: [], brands: [], who: [], minValue: '350', maxValue: '3750',});
    const fullFilters = {
        who: [ "child", "man", "woman" ],
        brands: [ "Levrana", "Chocolatte", "Cafe_Mimi", "ECOLAB" ],
        derm: [ "dry", "fat", "old", "sens", "comb" ],

    }

    let derm = computed(() => {
        return filters.derm.length ? filters.derm : fullFilters.derm
    });
    let brands = computed(() => {
        return filters.brands.length ? filters.brands : fullFilters.brands
    });
    let who = computed(() => {
        return filters.who.length ? filters.who : fullFilters.who
    });

    let cards = ref([]);

    watch(filters, async () => {
        if (parseInt(filters.minValue) > parseInt(filters.maxValue)) {
            let tmp = filters.minValue;
            filters.minValue = filters.maxValue;
            filters.maxValue = tmp;
        }
        const urlToCards = `http://127.0.0.1:8000/api/products/?d=${derm.value}&b=${brands.value}&w=${who.value}&p=${[filters.minValue, filters.maxValue]}`;
        cards.value.length = 0;
        let response = await fetchApi(urlToCards);
        response = response.data.value.data;
        cards.value.push(...response);
    });

    const fetchApi = async (url) => {
        return useFetch(url, {
            onResponse ({ request, options, response}) {
                return response._data
            },
        })
    }
    const fillFilter = (e) => {
        let filter =  e.target.value;
        if (filters[filter].length == 0) {
            filters[filter].push(...fullFilters[filter]);
            return
        }
        filters[filter].length = 0;
    }
    onMounted(async () => {
        setTimeout(async () => {
            const urlToCards = `http://127.0.0.1:8000/api/products/?d=${fullFilters.derm}&b=${fullFilters.brands}&w=${fullFilters.who}`;
            let response = await fetchApi(urlToCards);
            response = response.data.value.data;
            cards.value.push(...response);
        }, 1000);
    })
    const bindMinValue = (event) => {
        filters.minValue = event.target.value;
    }
    const bindMaxValue = (event) => {
        filters.maxValue = event.target.value;
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
        min-width: 190px;
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
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
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
    .card-grid {
        display: grid;
        /* grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); */
        grid-template-columns: 1fr 1fr 1fr;
        grid-gap: 30px;
        justify-content: center;
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
    .price-range {
        width: 100%;
        position: relative;
        margin: 22px 0 40px;
    }
    input[type='range'] {
        width: 100%;
        -webkit-appearance: none;
        -moz-appearance:none;
        background: transparent; 
        position: absolute;
        left: 0;
    }
    input[type='range']::-webkit-slider-thumb {
        -webkit-appearance:none;
        height: 14px;
        width: 14px;
        border-radius: 0;
        background: var(--color-accent);
        cursor: pointer;
        margin-top: -6px;
        position: relative;
        z-index: 1;
    }
    input[type='range']::-moz-range-thumb {
        -moz-appearance:none;
        height: 14px;
        width: 14px;
        background: var(--color-accent);
        cursor: pointer;
        border-radius: 0;
        margin-top: -6px;
        position: relative;
        z-index: 1;
        border: none;
    }
    input[type=range]::-webkit-slider-runnable-track {
        width: 100%;
        height: 2px;
        background: var(--text-opacity);
        border: none;
    }
    input[type=range]::-moz-range-track {
        width: 100%;
        height: 2px;
        background: var(--text-opacity);
        border: none;
    }
    .display-range {
        text-align: center;
        font-size: 18px;
        margin-bottom: 10px;
    }
    @media screen and (max-width: 1250px) {
        .main-aside{
            flex-shrink: 1;
            width: 25%;
        }
    }
    @media screen and (max-width: 1080px) {

        .card-grid {
            grid-gap: 15px;
        } 
        .main-inner {
            flex-direction: column;
            align-items: center;
        }
        .main-aside {
            width: 90%;
            margin: 0 auto 20px;
        }
        .main {
            padding: 40px 0;
        }
        form {
            padding-left: 25px;
        }
        .main-category {
            margin: 0 0 25px;
        }
        .price-range {
            width: 70%;
            margin: 22px auto 50px;
        }
    }
    @media screen and (max-width: 768px) {
        .card-grid {
            /* grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); */
            grid-template-columns: 1fr 1fr;
        }
    }

    @media screen and (max-width: 492px) {
        .main-aside {
            width: 100%;
        }
        .card-grid {
            grid-gap: 10px;
        }
        .main-header {
            flex-wrap: wrap;
            gap: 25px;
        }
        .main-product {
            margin-right: 25px;
            
        }

    }
</style>