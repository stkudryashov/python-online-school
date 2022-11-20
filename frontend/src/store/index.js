import { createStore } from 'vuex'

import { AuthModule } from './modules/AuthModule.js'
import { SidebarModule } from './modules/SidebarModule.js'

const store = createStore({
  state () {
    return {
    }
  },
  modules: {
    AuthModule,
    SidebarModule
  }
})

export default store
