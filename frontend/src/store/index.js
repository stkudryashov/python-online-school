import { createStore } from 'vuex'

import { AuthModule } from './modules/AuthModule.js'


const store = createStore({
  state () {
    return {
    }
  },
  modules: {
    AuthModule
  }
})

export default store
