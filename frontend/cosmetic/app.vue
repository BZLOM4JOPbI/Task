<script setup lang="ts">
useHead({
    title: 'Catalogue',
    meta: [
        { name: 'description', content: 'Cosmetis catalogue' }
    ],
//   bodyAttrs: {
//     class: 'Wrap'
//   },
})
</script>
<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>
<style>
    .flex-col {
        display: flex;
        flex-direction: column;
    }
</style>
