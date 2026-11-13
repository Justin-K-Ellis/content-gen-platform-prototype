import { createBrowserRouter } from "react-router"
import Demo from "./pages/Demo"
import About from "./pages/About"
import RootLayout from "./layouts/RootLayout"
import Home from "./pages/Home"

const router = createBrowserRouter([
  {
    path: "/demo",
    Component: Demo,
  },
  {
    Component: RootLayout,
    children: [
      {
        index: true,
        Component: Home,
      },
      {
        path: "about",
        Component: About,
      },
      {
        path: "create",
        children: [
          {
            path: "ra",
            element: <div>RA</div>,
          },
          {
            path: "rbsk",
            element: <div>RBSK</div>,
          },
          {
            path: "rbsc",
            element: <div>RBSC</div>,
          },
          {
            path: "rc",
            element: <div>RC</div>,
          },
          {
            path: "la",
            element: <div>LA</div>,
          },
          {
            path: "lb",
            element: <div>LB</div>,
          },
          {
            path: "lc",
            element: <div>LC</div>,
          },
          {
            path: "ld",
            element: <div>LD</div>,
          },
        ],
      },
    ],
  },
])

export default router
