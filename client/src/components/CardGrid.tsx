import { buttonVariants } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

interface Props {
  titles: string[]
}

export default function CardGrid(props: Props) {
  return (
    <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
      {props.titles.map((title) => (
        <Card
          key={title}
          className="flex flex-row items-center justify-between bg-zinc-100"
        >
          <CardHeader>
            <CardTitle>{title}</CardTitle>
          </CardHeader>
          <CardContent>
            <a href="#" className={buttonVariants({ variant: "default" })}>
              Go
            </a>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
