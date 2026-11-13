import { buttonVariants } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { LinkData } from "@/types"

interface Props {
  linkData: LinkData[]
}

export default function CardGrid(props: Props) {
  return (
    <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
      {props.linkData.map((data) => (
        <Card
          key={data.text}
          className="flex flex-row items-center justify-between bg-zinc-100"
        >
          <CardHeader>
            <CardTitle>{data.text}</CardTitle>
          </CardHeader>
          <CardContent>
            <a
              href={`create/${data.url}`}
              className={buttonVariants({ variant: "default" })}
            >
              Go
            </a>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
