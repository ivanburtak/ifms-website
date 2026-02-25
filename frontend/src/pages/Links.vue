<template>
  <section class="container-custom py-8">
    <h1 class="text-4xl font-bold mb-2 text-slate-900">Корисні ресурси</h1>
    <p class="text-slate-600 mb-8">Збірка корисних посилань на проекти та ресурси спільноти.</p>

    <!-- Societies Section -->
    <div class="mb-12">
      <h2 class="text-2xl font-bold mb-6 text-slate-900">Інші товариства</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <a v-for="l in societies" :key="l.id" :href="l.url" target="_blank" class="bg-white border border-slate-200 hover:border-sky-400 hover:shadow-lg rounded-lg p-5 transition duration-200 group">
          <div class="flex items-start justify-between mb-2">
            <h3 class="font-semibold text-slate-900 group-hover:text-sky-600 transition">{{ l.title }}</h3>
            <span class="text-xl">→</span>
          </div>
          <p class="text-sm text-slate-600 truncate">{{ l.url }}</p>
        </a>
      </div>
    </div>

    <!-- Interesting Links Section -->
    <div>
      <h2 class="text-2xl font-bold mb-6 text-slate-900">Цікаві ресурси</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <a v-for="l in interesting" :key="l.id" :href="l.url" target="_blank" class="bg-gradient-to-br from-sky-50 to-blue-50 border border-sky-200 hover:border-sky-400 hover:shadow-lg rounded-lg p-5 transition duration-200 group">
          <div class="flex items-start justify-between mb-2">
            <h3 class="font-semibold text-slate-900 group-hover:text-sky-600 transition">{{ l.title }}</h3>
            <span class="text-xl">↗</span>
          </div>
          <p class="text-sm text-slate-600 truncate">{{ l.url }}</p>
        </a>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
export default {
  setup(){
    const links = ref([])
    const loading = ref(true)
    onMounted(async ()=>{
      try {
        const res = await axios.get('http://localhost:8000/api/links/')
        links.value = res.data
      } finally {
        loading.value = false
      }
    })
    const societies = computed(()=> links.value.filter(l=>l.category==='society'))
    const interesting = computed(()=> links.value.filter(l=>l.category==='interesting'))
    return { links, societies, interesting, loading }
  }
}
</script>
