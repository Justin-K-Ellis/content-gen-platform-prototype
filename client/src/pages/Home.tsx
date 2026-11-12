import Heading1 from "@/components/Heading1"
import Heading2 from "@/components/Heading2"
import CardGrid from "@/components/CardGrid"

const readingCards = ["RA", "RBSK", "RBSC", "RC"]
const listeningCards = ["LA", "LB", "LC", "LD"]

export default function Home() {
  return (
    <section className="flex flex-col gap-8 p-4">
      <Heading1 text="Item Generator" />
      <div>
        <Heading2 text="Reading" />
        <CardGrid titles={readingCards} />
      </div>
      <div>
        <Heading2 text="Listening" />
        <CardGrid titles={listeningCards} />
      </div>
    </section>
  )
}
