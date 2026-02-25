<template>
  <section class="container-custom py-8">
    <!-- Toast Notification -->
    <div v-if="ok" class="fixed bottom-4 right-4 bg-green-50 border border-green-200 rounded-lg p-4 flex gap-3 shadow-lg max-w-sm z-50 animate-in">
      <span class="text-2xl flex-shrink-0">✓</span>
      <div>
        <h3 class="font-semibold text-green-900">Заявка надіслана!</h3>
        <p class="text-green-800 text-sm">Спасибі! Ми переглянемо вашу заявку і скоро зв'яжемось з вами.</p>
      </div>
      <button @click="ok = false" class="text-green-900 hover:text-green-700 font-bold">×</button>
    </div>

    <div class="max-w-2xl">
      <h1 class="text-4xl font-bold mb-2 text-slate-900">Подати заяву на вступ</h1>
      <p class="text-slate-600 mb-8">Приєднайтеся до нашої спільноти математиків. Заповніть форму нижче, і ми зв'яжемось з вами.</p>

      <form @submit.prevent="apply" class="space-y-6">
        <div>
          <label class="block text-sm font-semibold text-slate-900 mb-2">Ім'я</label>
          <input v-model="form.name" placeholder="Ваше ім'я" required class="w-full border border-slate-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-900 mb-2">Email</label>
          <input v-model="form.email" placeholder="your@email.com" type="email" required class="w-full border border-slate-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-slate-900 mb-2">Коротко про себе</label>
          <textarea v-model="form.message" placeholder="Розкажіть про себе, вашу спеціальність та причини вступу..." class="w-full border border-slate-300 rounded-lg px-4 py-3 h-32 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent resize-none"></textarea>
          <p class="text-sm text-slate-500 mt-1">Мінімум 10 символів</p>
        </div>

        <button type="submit" class="w-full px-6 py-3 bg-sky-600 hover:bg-sky-700 text-white rounded-lg font-semibold transition duration-200 flex items-center justify-center gap-2 !text-white">
          <span>Подати заяву</span>
          <span v-if="loading" class="inline-block animate-spin">↻</span>
        </button>
      </form>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import { reactive, ref } from 'vue'
export default {
  setup(){
    const form = reactive({ name:'', email:'', message:'' })
    const ok = ref(false)
    const loading = ref(false)
    const apply = async ()=>{
      try {
        loading.value = true
        await axios.post('http://localhost:8000/api/applications/', form)
        form.name = ''
        form.email = ''
        form.message = ''
        ok.value = true
        setTimeout(() => { ok.value = false }, 5000)
      } catch (e) {
        console.error(e)
      } finally {
        loading.value = false
      }
    }
    return { form, apply, ok, loading }
  }
}
</script>

