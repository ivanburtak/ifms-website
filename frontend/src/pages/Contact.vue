<template>
  <section class="container-custom py-8">
    <!-- Toast Notification -->
    <div v-if="sent" class="fixed bottom-4 right-4 bg-green-50 border border-green-200 rounded-lg p-4 flex gap-3 shadow-lg max-w-sm z-50 animate-in">
      <span class="text-2xl flex-shrink-0">✓</span>
      <div>
        <h3 class="font-semibold text-green-900">Повідомлення відправлене!</h3>
        <p class="text-green-800 text-sm">Дякуємо! Ми зв'яжемося з вами найближчим часом.</p>
      </div>
      <button @click="sent = false" class="text-green-900 hover:text-green-700 font-bold">×</button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl">
      <!-- Contact Form -->
      <div>
        <h1 class="text-3xl font-bold mb-2 text-slate-900">Зв'язатися з нами</h1>
        <p class="text-slate-600 mb-6">Маєте питання? Ми раді допомогти. Заповніть форму, і ми швидко відповімо.</p>

        <form @submit.prevent="send" class="space-y-4">
          <div>
            <label class="block text-sm font-semibold text-slate-900 mb-1">Ім'я</label>
            <input v-model="form.name" placeholder="Ваше ім'я" required class="w-full border border-slate-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent" />
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-900 mb-1">Email</label>
            <input v-model="form.email" placeholder="your@email.com" type="email" required class="w-full border border-slate-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent" />
          </div>

          <div>
            <label class="block text-sm font-semibold text-slate-900 mb-1">Повідомлення</label>
            <textarea v-model="form.message" placeholder="Напишіть своє повідомлення..." required class="w-full border border-slate-300 rounded-lg px-4 py-2 h-32 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent resize-none"></textarea>
          </div>

          <button type="submit" class="w-full px-6 py-3 bg-sky-600 hover:bg-sky-700 text-white rounded-lg font-semibold transition duration-200 flex items-center justify-center gap-2">
            <span>Відправити</span>
            <span v-if="loading" class="inline-block animate-spin">↻</span>
          </button>
        </form>
      </div>

      <!-- Contact Info -->
      <div>
        <h2 class="text-2xl font-bold mb-6 text-slate-900">Як з нами зв'язатися</h2>
        <div class="space-y-4">
          <div class="bg-slate-50 p-4 rounded-lg border border-slate-200">
            <div class="text-2xl mb-2">📧</div>
            <h3 class="font-semibold text-slate-900 mb-1">Email</h3>
            <a href="mailto:info@ifms.com" class="text-sky-600 hover:text-sky-700">info@ifms.com</a>
          </div>
          <div class="bg-slate-50 p-4 rounded-lg border border-slate-200">
            <div class="text-2xl mb-2">📍</div>
            <h3 class="font-semibold text-slate-900 mb-1">Адреса</h3>
            <p class="text-slate-700">Івано-Франківськ, Україна</p>
          </div>
          <div class="bg-slate-50 p-4 rounded-lg border border-slate-200">
            <div class="text-2xl mb-2">🕐</div>
            <h3 class="font-semibold text-slate-900 mb-1">Час роботи</h3>
            <p class="text-slate-700">Пн-Пт: 9:00 - 18:00</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import { reactive, ref } from 'vue'
export default {
  setup(){
    const form = reactive({ name:'', email:'', message:'' })
    const sent = ref(false)
    const loading = ref(false)
    const send = async ()=>{
      try {
        loading.value = true
        await axios.post('http://localhost:8000/api/contacts/', form)
        form.name = ''
        form.email = ''
        form.message = ''
        sent.value = true
        setTimeout(() => { sent.value = false }, 5000)
      } catch (e) {
        console.error(e)
      } finally {
        loading.value = false
      }
    }
    return { form, send, sent, loading }
  }
}
</script>
