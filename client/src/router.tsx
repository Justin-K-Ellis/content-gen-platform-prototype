import { createBrowserRouter } from "react-router"
import Demo from "./pages/Demo"

const router = createBrowserRouter([
  {
    path: "/demo",
    Component: Demo,
  },
])

export default router
