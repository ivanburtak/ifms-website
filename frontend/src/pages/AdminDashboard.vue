<template>
  <section class="container-custom py-10">
    <h1 class="text-2xl font-bold mb-6">Заяви на вступ</h1>
    <!-- Loading -->
    <div v-if="loading" class="grid gap-4">
      <div v-for="i in 3" :key="i" class="card-custom animate-pulse h-24"></div>
    </div>

    <!-- Applications -->
    <div v-else-if="applications.length > 0" class="grid gap-6">
      <div v-for="app in applications" :key="app.id"
        class="bg-white border border-slate-200 rounded-lg p-6 hover:shadow-lg transition">

        <div class="flex justify-between items-start mb-3">
          <h3 class="font-bold text-lg text-slate-900">
            {{ app.name }} ({{ app.email }})
          </h3>

          <span class="px-3 py-1 text-sm rounded-full" :class="statusClass(app.status)">
            {{ app.status }}
          </span>
        </div>

        <p class="text-slate-600 mb-2">
          {{ app.message }}
        </p>

        <p class="text-slate-400 text-sm mb-4">
          📅 {{ formatDate(app.created_at) }}
        </p>

        <div class="flex gap-2">
          <button @click="approve(app.id)"
            class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition">
            Прийняти
          </button>

          <button @click="reject(app.id)"
            class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition">
            Відхилити
          </button>
        </div>
      </div>
    </div>

    <!-- No applications -->
    <div v-else class="text-center py-12 text-slate-500">
      Немає нових заяв
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from "vue"
import axios from "axios"

export default {
  setup() {
    const applications = ref([])
    const loading = ref(true)
    const api = import.meta.env.VITE_API_URL

    const statusClass = (status) => {
      return {
        'bg-yellow-100 text-yellow-700': status === 'pending',
        'bg-green-100 text-green-700': status === 'approved',
        'bg-red-100 text-red-700': status === 'rejected'
      }
    }

    const formatDate = (date) => date ? new Date(date).toLocaleString('uk-UA') : '—'

    const approve = async (id) => {
      const token = localStorage.getItem("token")
      await axios.patch(`${api}/api/applications/${id}/`, { status: "approved" }, {
        headers: { Authorization: `Bearer ${token}` }
      })
      fetchApplications()
    }

    const reject = async (id) => {
      const token = localStorage.getItem("token")
      await axios.patch(`${api}/api/applications/${id}/`, { status: "rejected" }, {
        headers: { Authorization: `Bearer ${token}` }
      })
      fetchApplications()
    }

    const fetchApplications = async () => {
      try {
        const token = localStorage.getItem("token")
        const res = await axios.get(`${api}/api/applications/`, {
          headers: { Authorization: `Bearer ${token}` }
        })
        applications.value = res.data
      } catch (err) {
        console.error(err)
        localStorage.removeItem("token")
      } finally {
        loading.value = false
      }
    }

    onMounted(fetchApplications)

    return { applications, loading, statusClass, formatDate, approve, reject }
  }
}
</script>