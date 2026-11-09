import { createBrowserRouter } from "react-router"
import Test from "./pages/Test"

const router = createBrowserRouter([
  {
    path: "/",
    Component: Test,
  },
])

export default router
