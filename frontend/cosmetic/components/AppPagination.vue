<!-- <template>
    <div class="main-pagination">
        <div class="arrow-left" @click="pageDecrement, activePage($event)"><img src="/img/icons/page-left.svg" alt=""></div>
        <span @click="pageChange">{{ pages[0] }}</span>
        <span @click="">{{ pages[1] }}</span>
        <span @click="">{{ pages[2] }}</span>
        <span>...</span>
        <span @click="">{{ pages[3] }}</span>
        <span @click="">{{ pages[4] }}</span>
        <span @click="">{{ pages[5] }}</span>
        <div class="arrow-right" @click="pageIncrement"><img src="/img/icons/page-left.svg" alt=""></div>
    </div>
</template>
<script setup>
    import { ref } from 'vue'
    const pages = ref([1, 2, 3, 8, 9, 10]);
    const pageIncrement = () => {
        for (let i = 0; i < pages.value.length; i++) {
            pages.value[i] = ++pages.value[i];
        }
    }
    const pageDecrement = () => {
        for (let i = 0; i < pages.value.length; i++) {
            pages.value[i] = --pages.value[i];
        }
    }
    const activePage = (event) => {
        event.currentTarget.style.backgroundColor = '#F2E2D0';
    }
</script>
<style scoped>
    div span, .arrow-left, .arrow-right {
        padding: 9px 17px;
        border: 1px solid var(--color-focus);
        cursor: pointer;
    }
    .main-pagination {
        display: flex;
        width: fit-content;
        margin: 50px 0 0 auto;
    }
    .arrow-left, .arrow-right {
        padding: 9px;
        display: inline-block;
    }
    .arrow-left img, .arrow-right img {
        display: block;
    }
    .arrow-right {
        transform: rotate(180deg);
    }
</style> -->
<script setup>
    import { ref } from "vue";

    const send = defineEmits(['clicked']);

    const onClickHandler = function (page) {
        send('clicked', page);
    };

  const currentPage = ref(1);
</script>

<template>
<vue-awesome-paginate
    :total-items="90"
    :items-per-page="9"
    :max-pages-shown="3"
    v-model="currentPage"
    :on-click="onClickHandler"
>  
  <template #prev-button>
    <span>
        <img src="/img/icons/page-left.svg" />
    </span>
  </template>
  <template #next-button>
    <span>
      <img src="/img/icons/page-left.svg" style="transform: rotate(180deg);"/>
    </span>
  </template>
</vue-awesome-paginate>
</template>

<style>
    .pagination-container {
        display: flex;
    }
    .paginate-buttons {
        padding: 9px 17px;
        cursor: pointer;
        background-color: #fff;
        border: 1px solid var(--color-focus);
        color: var(--text-common);
        font-size: 18px;
    }
    /* .paginate-buttons:hover {
        background-color: #d8d8d8;
    } */
    .active-page {
        background-color: var(--color-focus);
        border: 1px solid var(--color-focus);
        color: var(--text-common);
    }
    .active-page:hover, .paginate-buttons:hover {
        background-color: var(--color-focus);
    }
    .next-button, .back-button {
        padding: 9.5px;
    }

    @media screen and (max-width: 400px) {
        .paginate-buttons {
            padding: 8px 15px;
            font-size: 16px;
        }
        .next-button, .back-button {
            padding: 7.5px;
        }
    }
    @media screen and (max-width: 350px) {
        .paginate-buttons {
            padding: 8px 13px;
            font-size: 14px;
        }
        .next-button, .back-button {
            padding: 6px;
        }
    }
</style>