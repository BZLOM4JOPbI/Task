<template>
    <label>
        <input type="checkbox" :value="value" v-model="checked">{{ label }}
    </label>
</template>
<script setup>
    import { ref } from 'vue'
    const checked = ref([]);
    let props = defineProps(['label', 'value']);

    console.log(props);
</script>