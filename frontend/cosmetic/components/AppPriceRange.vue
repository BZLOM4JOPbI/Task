<template>
        <div class="price-range">
            <p class="display-range">{{ priceRange.minValue }} - {{ priceRange.maxValue }}</p>
            <input type="range" min="350" max="5000" step="50" v-model="priceRange.minValue">
            <input type="range" min="350" max="5000" step="50" v-model="priceRange.maxValue">
            <!-- @change="displayMaxValue"  @change="displayMinValue" -->
        </div>
</template>
<script setup>
    import { ref, watch, reactive } from 'vue'
    const priceRange = reactive({
        minValue: '350', maxValue: '3750',
    })
    watch(priceRange, () => {
        if (parseInt(priceRange.minValue) < parseInt(priceRange.maxValue)) return
        let tmp = priceRange.minValue;
        priceRange.minValue = priceRange.maxValue;
        priceRange.maxValue = tmp;
    })

        // const minValue = ref('350');
    // const maxValue = ref('3750');
    // watch(minValue, () => {
    //     if (parseInt(minValue.value) < parseInt(maxValue.value)) return
    //     let tmp = minValue.value;
    //     minValue.value = maxValue.value;
    //     maxValue.value = tmp;
    // })
    // watch(maxValue, () => {
    //     if (parseInt(minValue.value) < parseInt(maxValue.value)) return
    //     let tmp = minValue.value;
    //     minValue.value = maxValue.value;
    //     maxValue.value = tmp;
    // })

</script>
<style scoped>
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
    @media screen and (max-width: 1050px) {
        .price-range {
            width: 70%;
            margin: 22px auto 50px;
        }
    }
</style>