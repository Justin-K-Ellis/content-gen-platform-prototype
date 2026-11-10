import { createBrowserRouter } from "react-router"
import Demo from "./pages/Demo"
import About from "./pages/About"
import RootLayout from "./layouts/RootLayout"

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
        element: <p>Hello</p>,
      },
      {
        path: "about",
        Component: About,
      },
    ],
  },
])

export default router
