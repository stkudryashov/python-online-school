export const SidebarModule = {
  namespaced: true,
  state() {
    return {
      isCollapsed: JSON.parse(localStorage.getItem('sidebarIsCollapsed'))
    }
  },
  getters: {
    getSidebarStatus(state) {
      return state.isCollapsed
    }
  },
  mutations: {
    setSidebarStatus (state) {
      state.isCollapsed = !state.isCollapsed
    }
  },
  actions: {
    changeSidebarStatus({commit, state}) {
      commit('setSidebarStatus')
      localStorage.setItem('sidebarIsCollapsed', JSON.stringify(state.isCollapsed))
    }
  }
}
