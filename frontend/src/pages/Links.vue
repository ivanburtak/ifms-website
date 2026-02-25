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
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const dummyLinks = [
  {
    id: 1,
    title: 'Український математичний журнал',
    url: 'https://umj.imath.kiev.ua/',
    category: 'society'
  },
  {
    id: 2,
    title: 'Львівське математичне товариство',
    url: 'https://iamm.lviv.ua/',
    category: 'society'
  },
  {
    id: 3,
    title: 'НАН України - Інститут прикладної математики',
    url: 'https://www.iamm.ivano-frankivsk.com/',
    category: 'society'
  },
  {
    id: 4,
    title: 'OEIS - Енциклопедія послідовностей цілих чисел',
    url: 'https://oeis.org/',
    category: 'interesting'
  },
  {
    id: 5,
    title: 'Project Euler - Математичні задачі',
    url: 'https://projecteuler.net/',
    category: 'interesting'
  },
  {
    id: 6,
    title: 'Art of Problem Solving',
    url: 'https://artofproblemsolving.com/',
    category: 'interesting'
  },
  {
    id: 7,
    title: 'Khan Academy - Математика',
    url: 'https://www.khanacademy.org/',
    category: 'interesting'
  },
  {
    id: 8,
    title: 'Wolfram MathWorld',
    url: 'https://mathworld.wolfram.com/',
    category: 'interesting'
  }
]

export default {
  setup(){
    const links = ref([])
    const loading = ref(false)
    const useDummyData = import.meta.env.VITE_USE_DUMMY_DATA === 'true'
    const societies = computed(()=> links.value.filter(l=>l.category==='society'))
    const interesting = computed(()=> links.value.filter(l=>l.category==='interesting'))

    onMounted(async () => {
      if (useDummyData) {
        links.value = dummyLinks
        return
      }

      loading.value = true
      try {
        const api = import.meta.env.VITE_API_URL || 'http://localhost:8000'
        const response = await axios.get(`${api}/api/links/`)
        links.value = response.data
      } catch (error) {
        console.error('Failed to load links:', error)
        links.value = dummyLinks
      } finally {
        loading.value = false
      }
    })

    return { links, societies, interesting, loading }
  }
}
</script>
