import { createStore } from 'vuex'

import { AuthModule } from './modules/AuthModule.js'
import { SidebarModule } from './modules/SidebarModule.js'
import { ThemeModule } from './modules/ThemeModule.js'

const store = createStore({
  state () {
    return {
    }
  },
  modules: {
    AuthModule,
    SidebarModule,
    ThemeModule
  }
})

export default store
