import { createBrowserRouter } from "react-router"
import Demo from "./pages/Demo"
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
        path: "bye",
        element: <p>Bye</p>,
      },
    ],
  },
])

export default router
