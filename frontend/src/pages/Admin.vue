<template>
  <div class="container-custom py-10">
    <div v-if="loading" class="text-center py-12 text-slate-500">
      Перевірка автентифікації...
    </div>

    <div v-else>
      <AdminLogin v-if="!isAuthenticated" @login-success="onLoginSuccess" />

      <AdminDashboard v-else />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue"
import axios from "axios"
import AdminLogin from "./AdminLogin.vue"
import AdminDashboard from "./AdminDashboard.vue"

export default {
  components: { AdminLogin, AdminDashboard },
  setup() {
    const isAuthenticated = ref(false)
    const loading = ref(true)
    const api = import.meta.env.VITE_API_URL

    const checkAuth = async () => {
      const token = localStorage.getItem("token")
      if (!token) {
        isAuthenticated.value = false
        loading.value = false
        return
      }

      try {
        await axios.get(`${api}/api/user/`, {
          headers: { Authorization: `Bearer ${token}` }
        })
        isAuthenticated.value = true
      } catch {
        localStorage.removeItem("token")
        isAuthenticated.value = false
      } finally {
        loading.value = false
      }
    }

    const onLoginSuccess = () => {
      isAuthenticated.value = true
    }

    onMounted(checkAuth)

    return { isAuthenticated, loading, onLoginSuccess }
  }

}
</script>