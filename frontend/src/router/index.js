import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Album from '@/components/Album'
import Event from '@/components/Event'
import Videos from '@/components/Videos'
import Video from '@/components/Video'
import Schedule from '@/components/Schedule'
import Map from '@/components/Map'
import Supporters from '@/components/Supporters'
import SupportersWrite from '@/components/SupportersWrite'
import SupportersView from '@/components/SupportersView'
import Toto from '@/components/Toto'
import TotoWrite from '@/components/TotoWrite'
import Login from '@/components/Login'
import SupportersCheck from '@/components/Internal/Supporters'
import TotoCheck from '@/components/Internal/Toto'
import StatusUpdate from '@/components/Internal/Events'
import ScheduleUpdate from '@/components/Internal/Schedule'
import CheerMessage from '@/components/CheerMessage'
import CheerMessageForm from '@/components/CheerMessageForm'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        contents: Home
      }
    },
    {
      path: '/album',
      name: 'album',
      components: {
        contents: Album
      }
    },
    {
      path: '/events/:id',
      name: 'event',
      components: {
        contents: Event
      }
    },
    {
      path: '/videos',
      name: 'videos',
      components: {
        contents: Videos
      }
    },
    {
      path: '/videos/:id',
      name: 'video',
      components: {
        contents: Video
      }
    },
    {
      path: '/schedule',
      name: 'schedule',
      components: {
        contents: Schedule
      }
    },
    {
      path: '/map',
      name: 'map',
      components: {
        contents: Map
      }
    },
    {
      path: '/login',
      name: 'login',
      components: {
        contents: Login
      }
    },
    {
      path: '/supporters',
      name: 'supporters',
      components: {
        contents: Supporters
      }
    },
    {
      path: '/supporters/write',
      name: 'supporters_write',
      components: {
        contents: SupportersWrite
      }
    },
    {
      path: '/supporters/:id',
      name: 'supporters_view',
      components: {
        contents: SupportersView
      }
    },
    {
      path: '/internal/supporters',
      name: 'supporters_check',
      components: {
        contents: SupportersCheck
      }
    },
    {
      path: '/toto',
      name: 'toto',
      components: {
        contents: Toto
      }
    },
    {
      path: '/toto/write',
      name: 'toto_write',
      components: {
        contents: TotoWrite
      }
    },
    {
      path: '/internal/toto',
      name: 'toto_check',
      components: {
        contents: TotoCheck
      }
    },
    {
      path: '/internal/events',
      name: 'status_update',
      components: {
        contents: StatusUpdate
      }
    },
    {
      path: '/internal/schedule',
      name: 'schedule_update',
      components: {
        contents: ScheduleUpdate
      }
    },
    {
      path: '/cheermessage',
      name: 'cheermessage',
      components: {
        contents: CheerMessage
      }
    },
    {
      path: '/cheermessage/write',
      name: 'cheermessage-write',
      components: {
        contents: CheerMessageForm
      }
    }
  ]
})
