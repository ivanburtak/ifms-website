<template>
  <section class="container-custom flex items-center justify-center py-16">
    <div class="bg-white border border-slate-200 rounded-lg p-8 w-full max-w-md shadow-sm">

      <h1 class="text-2xl font-bold text-slate-900 mb-6 text-center">
        Вхід для адміністратора
      </h1>

      <form @submit.prevent="login" class="space-y-4">

        <div>
          <label class="block text-sm text-slate-600 mb-1">Користувач</label>
          <input v-model="username" type="text"
            class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-sky-500">
        </div>

        <div>
          <label class="block text-sm text-slate-600 mb-1">Пароль</label>
          <input v-model="password" type="password"
            class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-sky-500">
        </div>

        <button type="submit"
          class="w-full bg-sky-600 text-white py-2 rounded-lg font-medium hover:bg-sky-700 transition">
          Увійти
        </button>

        <p v-if="error" class="text-red-500 text-sm text-center">
          Невірний логін або пароль
        </p>

      </form>

    </div>
  </section>
</template>

<script>
import axios from "axios"
import { ref } from "vue"

export default {
  props: {
    onLoginSuccess: Function
  },
  setup(props) {
    const username = ref("")
    const password = ref("")
    const error = ref(null)
    const api = import.meta.env.VITE_API_URL

    const login = async () => {
      error.value = null
      try {
        const res = await axios.post(`${api}/api/admin-login/`, {
          username: username.value,
          password: password.value,
        })
        localStorage.setItem("token", res.data.access)
        props.onLoginSuccess()
      } catch (err) {
        console.error(err)
        error.value = "Невірні дані для входу"
      }
    }

    return { username, password, login, error }
  },
}
</script>