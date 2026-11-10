import { Outlet } from "react-router"
import Navbar from "@/components/Navbar"

export default function RootLayout() {
  return (
    <>
      <Navbar />
      <main className="mx-auto w-11/12 md:w-6/12">
        <Outlet />
      </main>
    </>
  )
}
