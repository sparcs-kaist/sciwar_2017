import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Introduction from '@/components/Introduction'
import Album from '@/components/Album'
import Event from '@/components/Event'
import Videos from '@/components/Videos'
import VideosCheck from '@/components/Internal/VideosCheck'
import VideoUpdate from '@/components/Internal/VideoUpdate'
import VideoAdd from '@/components/Internal/VideoAdd'
import Video from '@/components/Video'
import Schedule from '@/components/Schedule'
import Map from '@/components/Map'
import Supporters from '@/components/Supporters'
import SupportersWrite from '@/components/SupportersWrite'
import SupportersView from '@/components/SupportersView'
import InternalSupportersView from '@/components/Internal/SupportersView'
import Toto from '@/components/Toto'
import TotoWrite from '@/components/TotoWrite'
import TotoView from '@/components/TotoView'
import InternalTotoView from '@/components/Internal/TotoView'
import Login from '@/components/Login'
import SupportersCheck from '@/components/Internal/Supporters'
import TotoCheck from '@/components/Internal/Toto'
import StatusUpdate from '@/components/Internal/Events'
import CheerMessage from '@/components/CheerMessage'
import CheerMessageForm from '@/components/CheerMessageForm'
import InternalHome from '@/components/Internal/Home'

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
      path: '/introduction',
      name: 'introduction',
      components: {
        contents: Introduction
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
      path: '/internal/videos',
      name: 'videos_check',
      components: {
        contents: VideosCheck
      }
    },
    {
      path: '/internal/videos/:id',
      name: 'video_update',
      components: {
        contents: VideoUpdate
      }
    },
    {
      path: '/internal/videos/add',
      name: 'video_add',
      components: {
        contents: VideoAdd
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
      path: '/internal/supporters/:id',
      name: 'internal_supporters_view',
      components: {
        contents: InternalSupportersView
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
      path: '/toto/:id',
      name: 'toto_view',
      components: {
        contents: TotoView
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
      path: '/internal/toto/:id',
      name: 'internal_toto_view',
      components: {
        contents: InternalTotoView
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
      path: '/cheermessage',
      name: 'cheermessage',
      components: {
        contents: CheerMessage
      }
    },
    {
      path: '/cheermessage/write',
      name: 'cheermessage_write',
      components: {
        contents: CheerMessageForm
      }
    },
    {
      path: '/internal',
      name: 'internal_home',
      components: {
        contents: InternalHome
      }
    }
  ]
})
