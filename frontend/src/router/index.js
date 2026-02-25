import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Events from '../pages/Events.vue'
import Members from '../pages/Members.vue'
import Links from '../pages/Links.vue'
import Contact from '../pages/Contact.vue'
import Apply from '../pages/Apply.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/events', component: Events },
    { path: '/members', component: Members },
    { path: '/links', component: Links },
    { path: '/contact', component: Contact },
    { path: '/apply', component: Apply },
]

const router = createRouter({ history: createWebHistory(import.meta.env.BASE_URL), routes })
export default router
