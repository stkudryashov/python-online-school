export const ThemeModule = {
  namespaced: true,
  state() {
    return {
      darkMode: JSON.parse(localStorage.getItem('darkMode'))
    }
  },
  getters: {
    isDarkMode(state) {
      return state.darkMode
    }
  },
  mutations: {
    setTheme (state) {
      state.darkMode = !state.darkMode
    }
  },
  actions: {
    changeTheme({commit, state}) {
      commit('setTheme')
      localStorage.setItem('darkMode', JSON.stringify(state.darkMode))
    }
  }
}
