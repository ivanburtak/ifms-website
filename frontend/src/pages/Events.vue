<template>
  <section class="container-custom">
    <h1 class="text-2xl font-bold mb-4">Події</h1>
    <nav class="flex flex-wrap gap-2 mb-4">
      <button @click="filter('all')" :class="kind==='all'?activeBtn:btn">Всі</button>
      <button @click="filter('conference')" :class="kind==='conference'?activeBtn:btn">Конференції</button>
      <button @click="filter('seminar')" :class="kind==='seminar'?activeBtn:btn">Семінари</button>
      <button @click="filter('workshop')" :class="kind==='workshop'?activeBtn:btn">Воркшопи</button>
      <button @click="filter('webinar')" :class="kind==='webinar'?activeBtn:btn">Вебінари</button>
    </nav>
    <div v-if="loading" class="grid gap-4">
      <div v-for="i in 3" :key="i" class="card-custom animate-pulse">
        <div class="h-6 bg-slate-300 rounded w-3/4 mb-2"></div>
        <div class="h-4 bg-slate-300 rounded w-1/2 mb-2"></div>
        <div class="h-20 bg-slate-300 rounded"></div>
      </div>
    </div>
    <div v-else-if="filtered.length > 0" class="grid gap-6">
      <div v-for="e in filtered" :key="e.id" class="bg-white border border-slate-200 rounded-lg p-6 hover:shadow-lg transition duration-200">
        <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-3 mb-3">
          <h3 class="text-xl font-bold text-slate-900">{{ e.title }}</h3>
          <span class="px-3 py-1 bg-sky-100 text-sky-700 rounded-full text-sm font-medium whitespace-nowrap">{{ getCategoryLabel(e.type) }}</span>
        </div>
        <p class="text-sm text-slate-500 mb-3 flex items-center gap-2">
          <span>📅</span> {{ formatDate(e.date) }}
        </p>
        <p class="text-slate-700 leading-relaxed">{{ e.description }}</p>
      </div>
    </div>
    <div v-else class="text-center py-12">
      <p class="text-slate-600 text-lg">Немає подій у цій категорії</p>
    </div>
  </section>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const dummyEvents = [
  {
    id: 1,
    title: 'Міжнародна конференція з чистої математики',
    type: 'conference',
    date: '2026-04-15T10:00:00',
    description: 'Конференція присвячена найновішим тенденціям у чистій математиці. Учасники поділяться своїми дослідженнями та знаходитимуть нові напрямки для розвитку науки.'
  },
  {
    id: 2,
    title: 'Семінар: Топологія та її застосування',
    type: 'seminar',
    date: '2026-03-20T14:30:00',
    description: 'Обговорення сучасних методів топологічного аналізу та їхніх практичних застосувань у фізиці та комп\'ютерних науках.'
  },
  {
    id: 3,
    title: 'Воркшоп: Численні методи',
    type: 'workshop',
    date: '2026-03-10T09:00:00',
    description: 'Практичний семінар з розробки та реалізації чисельних методів розв\'язання складних математичних задач.'
  },
  {
    id: 4,
    title: 'Вебінар: Штучний інтелект та математика',
    type: 'webinar',
    date: '2026-02-28T18:00:00',
    description: 'Онлайн зустріч, присвячена взаємозв\'язку між математичними основами та розвитком штучного інтелекту.'
  },
  {
    id: 5,
    title: 'Конференція студентів-математиків',
    type: 'conference',
    date: '2026-05-05T11:00:00',
    description: 'Платформа для молодих математиків представити свої дослідження та отримати зворотний зв\'язок від професіоналів.'
  },
  {
    id: 6,
    title: 'Семінар: Аналіз великих даних',
    type: 'seminar',
    date: '2026-04-01T16:00:00',
    description: 'Огляд математичних підходів до обробки та аналізу великих обсягів даних.'
  }
]

export default {
  setup(){
    const events = ref([])
    const kind = ref('all')
    const loading = ref(false)
    const useDummyData = import.meta.env.VITE_USE_DUMMY_DATA === 'true'
    const btn = 'px-4 py-2 bg-white rounded-lg text-slate-700 border border-slate-300 hover:border-slate-400 transition font-medium'
    const activeBtn = 'px-4 py-2 bg-sky-600 text-white rounded-lg transition font-medium'
    const filter = (k) => kind.value = k
    const filtered = computed(() => {
      if (kind.value === 'all') return events.value
      return events.value.filter(e=>e.type===kind.value)
    })
    const formatDate = (d)=> d ? new Date(d).toLocaleString('uk-UA') : '—'
    const getCategoryLabel = (type) => {
      const labels = {
        'conference': 'Конференція',
        'seminar': 'Семінар',
        'workshop': 'Воркшоп',
        'webinar': 'Вебінар'
      }
      return labels[type] || type
    }

    onMounted(async () => {
      if (useDummyData) {
        events.value = dummyEvents
        return
      }

      loading.value = true
      try {
        const api = import.meta.env.VITE_API_URL || 'http://localhost:8000'
        const response = await axios.get(`${api}/api/events/`)
        events.value = response.data
      } catch (error) {
        console.error('Failed to load events:', error)
        events.value = dummyEvents
      } finally {
        loading.value = false
      }
    })

    return { events, kind, filter, filtered, formatDate, btn, activeBtn, loading, getCategoryLabel }
  }
}
</script>
