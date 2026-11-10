import { Link } from "react-router"
import { buttonVariants } from "@/components/ui/button"
import type { LinkData } from "@/types"

export default function Navbar() {
  const links: LinkData[] = [
    { url: "/", text: "Home" },
    { url: "about", text: "About" },
  ]

  return (
    <nav className="mb-4 flex items-center justify-between px-4 py-2 shadow md:mb-8">
      <Link to={"/"} className="text-lg font-semibold">
        Item Generator
      </Link>
      <div className="flex gap-2 md:gap-4">
        {links.map((link) => (
          <Link
            key={link.url}
            to={link.url}
            className={buttonVariants({ variant: "outline" })}
          >
            {link.text}
          </Link>
        ))}
      </div>
    </nav>
  )
}
