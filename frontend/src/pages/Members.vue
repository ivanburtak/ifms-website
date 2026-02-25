<template>
  <section class="container-custom">
    <h1 class="text-2xl font-bold mb-4">Члени товариства</h1>
    <div v-if="loading" class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
      <div v-for="i in 6" :key="i" class="bg-white rounded-lg overflow-hidden animate-pulse">
        <div class="w-full h-40 bg-slate-300"></div>
        <div class="p-4">
          <div class="h-5 bg-slate-300 rounded w-3/4 mb-2"></div>
          <div class="h-4 bg-slate-300 rounded"></div>
        </div>
      </div>
    </div>
    <div v-else class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
      <div class="bg-white border border-slate-200 rounded-lg overflow-hidden hover:shadow-lg transition duration-200" v-for="m in members" :key="m.id">
        <img v-if="m.photo_url" :src="m.photo_url" alt="photo" class="w-full h-40 object-cover" />
        <div v-else class="w-full h-40 bg-gradient-to-br from-slate-200 to-slate-300 flex items-center justify-center text-4xl text-slate-400">👤</div>
        <div class="p-5">
          <h3 class="font-bold text-slate-900 text-lg">{{ m.name }}</h3>
          <p class="text-slate-600 text-sm mt-2 leading-relaxed">{{ m.bio || 'Активний член товариства' }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const dummyMembers = [
  {
    id: 1,
    name: 'Іван Петренко',
    bio: 'Професор математики, спеціаліст у галузі алгебри та теорії чисел.',
    photo_url: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Ivan'
  },
  {
    id: 2,
    name: 'Марія Коваленко',
    bio: 'Доцент, дослідниця в області диференціальних рівнянь.',
    photo_url: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Maria'
  },
  {
    id: 3,
    name: 'Дмитро Сидоренко',
    bio: 'Аспірант, займається геометричним аналізом.',
    photo_url: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Dmytro'
  },
  {
    id: 4,
    name: 'Олена Шевченко',
    bio: 'Викладачка, експертиза у області викладання математики.',
    photo_url: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Olena'
  },
  {
    id: 5,
    name: 'Сергій Морозов',
    bio: 'Молодий вчений, дослідження у галузі комбінаторики.',
    photo_url: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Sergiy'
  },
  {
    id: 6,
    name: 'Анна Гончаренко',
    bio: 'Експертиза у числовому аналізі та обчислювальній математиці.',
    photo_url: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Anna'
  }
]

export default {
  setup(){
    const members = ref([])
    const loading = ref(false)
    const useDummyData = import.meta.env.VITE_USE_DUMMY_DATA === 'true'

    onMounted(async () => {
      if (useDummyData) {
        members.value = dummyMembers
        return
      }

      loading.value = true
      try {
        const api = import.meta.env.VITE_API_URL || 'http://localhost:8000'
        const response = await axios.get(`${api}/api/members/`)
        members.value = response.data
      } catch (error) {
        console.error('Failed to load members:', error)
        members.value = dummyMembers
      } finally {
        loading.value = false
      }
    })

    return { members, loading }
  }
}
</script>
