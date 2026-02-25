<template>
  <div class="min-h-screen bg-slate-50 flex flex-col">
    <Navbar />
    <main class="flex-1">
      <router-view />
    </main>
    <footer class="bg-slate-900 text-slate-400 py-8 mt-12 border-t border-slate-800">
      <div class="container-custom">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-6">
          <div>
            <h3 class="text-white font-bold mb-3">IFMS</h3>
            <p class="text-sm leading-relaxed">Івано-Франківське математичне товариство</p>
          </div>
          <div>
            <h3 class="text-white font-bold mb-3">Навігація</h3>
            <ul class="text-sm space-y-2">
              <li><router-link to="/" class="hover:text-white transition">Головна</router-link></li>
              <li><router-link to="/events" class="hover:text-white transition">Події</router-link></li>
              <li><router-link to="/members" class="hover:text-white transition">Члени</router-link></li>
              <li><router-link to="/apply" class="hover:text-white transition">Подати заяву</router-link></li>
            </ul>
          </div>
          <div>
            <h3 class="text-white font-bold mb-3">Слідкуйте за нами</h3>
            <ul class="text-sm space-y-2">
              <li><a href="https://www.facebook.com" target="_blank" class="hover:text-white transition">Facebook</a></li>
              <li><a href="https://www.twitter.com" target="_blank" class="hover:text-white transition">Twitter</a></li>
              <li><a href="mailto:info@ifms.com" class="hover:text-white transition">Email</a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-slate-800 pt-6 text-center text-sm">
          <p>&copy; 2026 Івано-Франківське Математичне Товариство. Усі права застережені.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default { components: { Navbar } }
</script>
