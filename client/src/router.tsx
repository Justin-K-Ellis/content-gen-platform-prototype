import { createBrowserRouter } from "react-router"
import Demo from "./pages/Demo"
import About from "./pages/About"
import RootLayout from "./layouts/RootLayout"
import Home from "./pages/Home"
import CreateItem from "./pages/CreateItem"

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
        path: "create/:itemType",
        Component: CreateItem,
      },
    ],
  },
])

export default router
