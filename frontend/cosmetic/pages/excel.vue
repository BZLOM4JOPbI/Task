<template>
    <main class="main">
        <div class="container">
            <div class="main-inner">
                <form action="http://127.0.0.1:8000/api/products/" method="post">
                    <label>Еа, там ревели горы мама
                        <input type="file" enctype="multipart/form-data">
                    </label>
                </form>
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
</style>